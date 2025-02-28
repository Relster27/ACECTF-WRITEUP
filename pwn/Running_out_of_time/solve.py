#!/usr/bin/env python

def decrypt():
    local_28 = [0x1d, 0x1b, 0x47, 0x19, 0x75, 0x1f, 0x1d, 0x1a, 0x5a, 0x5a, 0x19, 0x4e]
    local_d = 0x2a
    
    decrypted = ''.join(chr(b ^ local_d) for b in local_28)
    print("Decrypted output:", decrypted)

if __name__ == "__main__":
    decrypt()

# FLAG = ACECTF{[decrypted]}
