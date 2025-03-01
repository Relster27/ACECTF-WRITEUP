#!/usr/bin/env python

def decrypt():
    FLAG = [0x1d, 0x1b, 0x47, 0x19, 0x75, 0x1f, 0x1d, 0x1a, 0x5a, 0x5a, 0x19, 0x4e]
    KEY = 0x2a
    
    decrypted = ''.join(chr(b ^ KEY) for b in FLAG)
    print("Decrypted output:", decrypted)

if __name__ == "__main__":
    decrypt()
