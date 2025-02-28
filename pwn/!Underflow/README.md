# Ret2win

Checking binary protection.
```bash
[*] '/home/relster/Desktop/ctf/acectf/pwn/underflow/exploit-me'
    Arch:       amd64-64-little
    RELRO:      No RELRO
    Stack:      No canary found
    NX:         NX unknown - GNU_STACK missing
    PIE:        No PIE (0x400000)
    Stack:      Executable
    RWX:        Has RWX segments
    Stripped:   No
```

Disassembled code in ghdira.
![image](https://github.com/user-attachments/assets/36abedb6-6e18-420f-9c53-5da615c38c3a)

![image](https://github.com/user-attachments/assets/0a01f11d-d6bf-4cb3-93aa-2c89da866c41)

This is a basic buffer overflow and return to _**win**_ function. Let's overflow the stack which holds 64 **bytes** and add extra 8 **bytes** for RBP and the 73rd byte is where RIP (instruction pointer) starts.
We could grab the address of _**win**_ function from gdb or use _**pwntools**_, here i'll just grab manually from gdb.
![image](https://github.com/user-attachments/assets/52e5e395-0959-42fd-8664-ab6ef3663f6d)

## Keyword
ret2win \
Buffer overflow 
