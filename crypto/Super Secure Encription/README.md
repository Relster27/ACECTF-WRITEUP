# Super Secure Encryption

A cryptographic challenge that demonstrates the dangers of keystream reuse in stream ciphers, specifically exploiting a vulnerability in AES-CTR mode implementation.

## Challenge Description

> I'm doing a big favour with this one... I'm handing out my super secure functionality to the outer world to stumble upon & explore. Though, I still remember one of my colleagues once saying that nothing in this world is secure nowadays but my script right here stands on the contrary. I'll give you the access to my arsenal and see if you can prove me wrong.

In this challenge, we're presented with a scenario where someone has implemented "super secure" encryption functionality using AES in Counter (CTR) mode. The creator is confident in their implementation's security, despite a colleague's warning that "nothing in this world is secure nowadays."

We're given two files:
1. `chall.py` - The encryption script used to generate the encrypted messages
2. `msg.txt` - A file containing two encrypted messages (in hex format)

Let's take a closer look at the encryption implementation in `chall.py`:

```python
from Crypto.Cipher import AES
from Crypto.Util import Counter
import os

k = os.urandom(16) # Is it too short?

def encrypt(plaintext):
    cipher = AES.new(k, AES.MODE_CTR, counter=Counter.new(128)) # I was told, CTR can't be broken!
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext.hex()

msg = b'This is just a test message and can totally be ignored.' # Just checking functionality
encrypted_msg = encrypt(msg)

with open('flag.txt', 'r') as f:
    flag = f.readline().strip().encode()

encrypted_flag = encrypt(flag)

with open('msg.txt', 'w+') as o:
    o.write(f"{encrypted_msg}\n")
    o.write(f"{encrypted_flag}")
```

The code encrypts two messages using AES in CTR mode:
1. A known test message: `This is just a test message and can totally be ignored.`
2. The flag (which we need to recover)

Both encrypted messages are written to `msg.txt` in hexadecimal format.

## Solution Process

### Understanding the Vulnerability

The critical flaw in this implementation is that it creates a new AES cipher object for each encryption call, but with the same key and counter configuration. In CTR mode, this means that the exact same keystream is generated and used for both encryptions!

CTR mode works by:
1. Generating a keystream by encrypting sequential counter values
2. XORing this keystream with the plaintext to produce the ciphertext

If the same keystream is used to encrypt two different messages, we can exploit this to recover the unknown message (in this case, the flag) if we know one of the messages.

### Mathematical Explanation

Let's call:
- P₁ = the known plaintext (test message)
- C₁ = the encrypted test message
- P₂ = the unknown plaintext (flag)
- C₂ = the encrypted flag
- K = the keystream

In CTR mode encryption:
- C₁ = P₁ ⊕ K
- C₂ = P₂ ⊕ K

If we know P₁ and C₁, we can derive K:
- K = P₁ ⊕ C₁

Then we can recover P₂:
- P₂ = C₂ ⊕ K

By substituting:
- P₂ = C₂ ⊕ (P₁ ⊕ C₁) = C₂ ⊕ P₁ ⊕ C₁

### Implementation

Let's implement the solution step by step. The provided `script.py` already contains the solution implementation:

```python
#!/usr/bin/env python3
from binascii import unhexlify

def xor_bytes(a, b):
    """XOR two byte arrays element-wise."""
    return bytes(x ^ y for x, y in zip(a, b))

def decrypt_flag():
    # Known plaintext that was encrypted
    known_plaintext = b'This is just a test message and can totally be ignored.'
    
    try:
        # Read ciphertexts from msg.txt
        with open('msg.txt', 'r') as f:
            lines = f.readlines()
            if len(lines) < 2:
                print("Error: msg.txt doesn't contain enough lines.")
                return
                
            known_ciphertext_hex = lines[0].strip()
            flag_ciphertext_hex = lines[1].strip()
            
        # Convert hex ciphertexts to bytes
        try:
            known_ciphertext = unhexlify(known_ciphertext_hex)
            flag_ciphertext = unhexlify(flag_ciphertext_hex)
        except:
            print("Error: Could not decode hex ciphertexts.")
            return
            
        # Derive keystream: plaintext XOR ciphertext
        keystream = xor_bytes(known_plaintext, known_ciphertext)
        
        # Recover flag: ciphertext XOR keystream
        # Use only as much of the keystream as we need
        flag = xor_bytes(flag_ciphertext, keystream[:len(flag_ciphertext)])
        
        # Try to decode the flag as ASCII or UTF-8
        try:
            decoded_flag = flag.decode('utf-8')
            print("Recovered flag:", decoded_flag)
        except:
            print("Warning: Couldn't decode the flag as UTF-8. Raw bytes:", flag)
            
    except FileNotFoundError:
        print("Error: msg.txt not found.")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")

if __name__ == "__main__":
    decrypt_flag()
```

Let's break down this solution:

1. We define a helper function `xor_bytes` that performs element-wise XOR on two byte arrays.

2. In the `decrypt_flag` function:
   - We start with the known plaintext from `chall.py`.
   - We read the two encrypted messages from `msg.txt`.
   - We convert the hexadecimal strings to bytes using `unhexlify`.
   - We derive the keystream by XORing the known plaintext with its corresponding ciphertext.
   - We recover the flag by XORing the flag ciphertext with the derived keystream.
   - We decode the recovered flag from bytes to a string.

3. The script includes comprehensive error handling for file operations, hex decoding, and string decoding.

### Executing the Solution

When we run the script with the provided `msg.txt`, it should successfully recover and print the flag:

```bash
$ python3 script.py
Recovered flag: ACECTF{n07h1n6_15_53cur3_1n_7h15_w0rld}
```


### Image Explain 

![image](https://github.com/user-attachments/assets/12096058-a72b-48f9-93e3-c60cd16b99c8)
