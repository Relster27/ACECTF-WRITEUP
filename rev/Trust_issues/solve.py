#!/usr/bin/env python3

def main():
    key = [
        0x06, 0x11, 0x1d, 0x72, 0x60, 0x1f, 0x18, 0x7c,
        0x3e, 0x0f, 0x6d, 0x78, 0x33, 0x35, 0x40, 0x5e,
        0x3e, 0x25, 0x5f, 0x30, 0x78, 0x14, 0x37, 0x4a
    ]
    
    enc = "GRX14YcKLzXOlW5iaSlBIrN7"
    
    original = ""
    for i in range(len(enc)):
        original += chr(ord(enc[i]) ^ key[i])
    
    print("Output:")
    print(original)

if __name__ == "__main__":
    main()
'''
NOTE:

  The challenge involved understanding a simple XOR encoding mechanism and reversing it to retrieve the correct input.
  
  The binary checks if the first command-line argument matches a specific string. However, instead of a direct comparison, 
  it uses a custom _strcmp function, which XORs each character of the input with a predefined byte array (local_20) and then compares it with the expected string "GRX14YcKLzXOlW5iaSlBIrN7".
'''
