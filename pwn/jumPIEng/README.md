![Screenshot 2025-03-01 120403](https://github.com/user-attachments/assets/a35642a4-a783-4b29-b56f-9686cba986ec)

# Technique : Ret2win (with leaked address)

## Analyze given file.
Given a binary (ELF) named _**redirection**_. \
Checking binary protection.
```bash
[*] '/home/relster/Desktop/ctf/acectf/pwn/jumPIEng/redirection'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        PIE enabled
    Stripped:   No
```
Almost all protections are enabled except **RELRO**. But the catch here is, we don't have to worry about any protection at all because our input (which in hexadecimal) is treats as a function pointer. So in this challenge we don't need to do overflow at all.

Decompiled binary in **Ghidra**:
![Screenshot 2025-03-01 123003](https://github.com/user-attachments/assets/1e5c47a2-9d2e-4c76-a706-4b6e1ee13b93)
>Note : The squared parts are the only important part we need to look at.

Checking **_win_** function offset in **_GDB_**.
```bash
gdb -q ./redirection
```
![image](https://github.com/user-attachments/assets/95fbe310-9f76-4afe-9142-30af6ed8276a) \
The offset is **_0x1262_** from the base address of the binary.

Since the program already leaking the base address of the binary, then we just need to add the offset of **_redirected_to_success()_** (**__0x1262__**) to the leaked address, and that's it, we've redirected execution to the _**win function**_ and get the flag.

## Result
![Screenshot 2025-03-01 123637](https://github.com/user-attachments/assets/ad377e79-1b73-42d8-9ce8-a98549075b70)

## Keyword
Ret2win \
Function offsets \
Extracting strings with pwntools



