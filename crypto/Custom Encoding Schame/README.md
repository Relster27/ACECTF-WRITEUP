# Custom Encoding Scheme

![image](https://github.com/user-attachments/assets/4e09bb99-1ad9-43b9-839b-f98f96dd18db)

## Challenge Description

> I wanted to create a custom encoding for a crypto challenge but turns out, I didn't have anough time on my hands. So, what I did here is - Well instead of explaining it to you why don't I give you the script?

The challenge provides two files: `encrypt.py` and `output.txt`. The Python script (`encrypt.py`) implements a custom encoding scheme that takes a plaintext message and encodes it using a modified Base64-like approach, incorporating bits from a redacted value (presumably the flag). The encoded output is stored in `output.txt`.

This suggests we need to understand the encoding algorithm and reverse it to recover the hidden flag.

## Solution Process

### 1. Understanding the Encoding Algorithm

First, let's analyze the `encrypt.py` script to understand how the encoding works:

```python
def e1(t, b, o):
    t1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    if len(b) != 168:
        raise ValueError("Invalid Input")
    c = [b[i:i+4] for i in range(0, len(b), 4)]
    with open(o, "w") as f:
        for x, y in enumerate(t):
            z = f"{ord(y):08b}"
            if x < 42:
                a = z[:6]
                d = z[6:] + c[x]
                e = int(a, 2)
                g = int(d, 2)
                r = t1[e] + t1[g]
            else:
                a = z[:6]
                d = z[6:]
                e = int(a, 2)
                g = int(d, 2)
                r = t1[e] + t1[g]
            print(r)
            f.write(r + "\n")

t = "I TOLD YOU THAT BASE64 DECODING IS NO GOOD"
b = "{REDACTED}" # Should be 128 bits
o = "output.txt"

e1(t, b, o)


```

Key observations from the encoding process:

1. The function uses a standard Base64 character set (`t1`)
2. It requires a binary string (`b`) that must be exactly 168 bits long
3. This binary string is split into 4-bit chunks (`c`)
4. For each character in the plaintext message (`t`):
   - It converts the character to its 8-bit binary representation (`z`)
   - For the first 42 characters:
     - It splits the binary into the first 6 bits (`a`) and last 2 bits (`d`)
     - It appends 4 bits from the redacted value (`c[x]`) to the last 2 bits
     - It converts these two 6-bit values to indices in the Base64 character set
     - The result is two Base64 characters for each original character
   - For characters beyond position 42, it performs a similar encoding but without using bits from the redacted value

The plaintext message used is: "I TOLD YOU THAT BASE64 DECODING IS NO GOOD"

### 2. Examining the Output

Looking at `output.txt`, we see a series of 2-character strings, each representing one character from the original message after encoding:

```
SU
IB
VE
Tz
TE
RF
IE
WT
T1
VU
IE
VG
SH
Qb
VD
IH
Qm
QY
Uz
RU
Nj
NH
IF
RP
RX
Q3
Tz
RE
ST
Tl
R1
IP
SW
Uz
ID
Tg
Tz
IA
R2
T8
T3
RN

```

### 3. Developing the Solution Strategy

Since we know both the plaintext and its encoded output, we can reverse the process to recover the redacted binary string. The strategy is:

1. For each character in the plaintext and its corresponding encoded pair:
   - Convert the plaintext character to its binary representation
   - Convert the encoded Base64 pair back to their 6-bit binary values
   - The first 6 bits should match the first 6 bits of the original character
   - The first 2 bits of the second 6-bit value should match the last 2 bits of the original character
   - The remaining 4 bits are from our redacted flag!

### 4. Implementing the Solution

The provided `script.py` implements this reverse engineering approach:

```python
def recover_flag():
    # Use the content provided in the challenge instead of reading from a file
    output_content = """SU
IB
VE
Tz
TE
RF
IE
WT
T1
VU
IE
VG
SH
Qb
VD
IH
Qm
QY
Uz
RU
Nj
NH
IF
RP
RX
Q3
Tz
RE
ST
Tl
R1
IP
SW
Uz
ID
Tg
Tz
IA
R2
T8
T3
RN"""

    encoded_pairs = output_content.strip().split('\n')

    # Define the same Base64 character set
    t1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    # Known plaintext
    plaintext = "I TOLD YOU THAT BASE64 DECODING IS NO GOOD"

    # To store the recovered bits
    recovered_bits = ""

    # Process each character
    for i, (char, encoded_pair) in enumerate(zip(plaintext, encoded_pairs)):
        if i >= 42:
            break  # We only care about the first 42 characters
        
        # Get the 8-bit binary representation of the plaintext character
        char_bin = f"{ord(char):08b}"
        
        # Get the indices in the Base64 set for the encoded pair
        first_char_index = t1.index(encoded_pair[0])
        second_char_index = t1.index(encoded_pair[1])
        
        # Convert indices back to binary
        first_part_bin = f"{first_char_index:06b}"
        second_part_bin = f"{second_char_index:06b}"
        
        # Verify the first part matches the first 6 bits of our plaintext char
        if first_part_bin != char_bin[:6]:
            print(f"Verification failed for character {i}: {char}")
        
        # Extract the 4 bits that were added from the redacted value
        # The last 2 bits of char_bin + 4 bits from redacted = second_part_bin
        last_2_bits_of_char = char_bin[6:]
        
        if second_part_bin[:2] != last_2_bits_of_char:
            print(f"Bit mismatch at position {i}: expected {last_2_bits_of_char} but got {second_part_bin[:2]}")
            
        redacted_4bits = second_part_bin[2:]
        
        # Add to our recovered bits
        recovered_bits += redacted_4bits

    print(f"Recovered {len(recovered_bits)} bits")
    
    # Use ALL the recovered bits (168 bits)
    binary_string = recovered_bits
    
    # Convert binary to text
    flag = ""
    for i in range(0, len(binary_string), 8):
        if i + 8 <= len(binary_string):
            byte = binary_string[i:i+8]
            flag += chr(int(byte, 2))
            
    print(f"Full Flag: {flag}")
    
    # Show hexadecimal representation
    hex_values = ""
    for i in range(0, len(binary_string), 4):
        if i + 4 <= len(binary_string):
            nibble = binary_string[i:i+4]
            hex_values += hex(int(nibble, 2))[2:]
            
    print(f"Hex: {hex_values}")
    
    return flag

if __name__ == "__main__":
    recover_flag()
```

### 5. Running the Solution and Obtaining the Flag

When executing the solution script, it:

1. Processes the first 42 characters from the plaintext and their corresponding encoded pairs
2. Extracts 4 bits from each encoded pair, resulting in 168 bits total (42 × 4)
3. Converts these bits to ASCII characters (8 bits per character)
4. Returns the recovered flag

The recovered flag would be a 21-character string (168 bits ÷ 8 bits per byte), representing the originally redacted value in the encryption script.

### Flag 

```
Recovered 168 bits
Full Flag: ACECTF{7h47_w45_c00l}
Hex: 4143454354467b376834375f7734355f6330306c7d
```
