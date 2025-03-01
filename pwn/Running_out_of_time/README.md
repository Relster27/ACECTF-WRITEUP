![image](https://github.com/user-attachments/assets/f85bb8d4-5bc0-49a4-b23e-d623d9240e07)

>Note : Unintended way to solve this? (IDK)

# POC
I don't know if this challenge supposed to have its own encryption algorithm embedded in the binary. But this challenge becomes a **reverse** challenge rather than **pwn**. But anyway.

## Analyze the binary
Decompiled binary in **Ghidra**. \
![image](https://github.com/user-attachments/assets/9201ff4d-6d3d-4c3a-9cb3-b62842f8a4ea) \
This program accepts user input and stores it into **_input_buf_** variable. The intended way to solve this is to guess the correct value and let the binary prints the flag itself. But rather than doing that, i reversed the encryption algorithm which is just a basic XOR encryption with a key.

Running **solve.py** gives us the flag. \
![Screenshot 2025-03-01 130253](https://github.com/user-attachments/assets/dd3461b2-3c93-420c-84c8-f75e2fcfdb5b)

FLAG = ACECTF{71m3_570pp3d}
