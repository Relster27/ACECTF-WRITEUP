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