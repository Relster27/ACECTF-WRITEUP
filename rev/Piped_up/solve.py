#!/usr/bin/env python

def mode1_reverse(data):
    result = bytearray(len(data))
    prev = 0
    for i in range(len(data)):
        result[i] = data[i] ^ prev
        prev = data[i]
    return result

def mode3_transform(data):
    return bytearray(b ^ 0x56 for b in data)

def mode5_reverse(data, key):
    return bytearray(data[i] ^ key[i % len(key)] for i in range(len(data)))

target = [
    0x6c, 0x2c, 0xe0, 0xef, 0x8d, 0x60, 0xdc, 0x75, 0x0d, 0xff, 0xd6, 0x59, 0xf4, 
    0x5d, 0xde, 0x9b, 0xe3, 0xd7, 0x52, 0x99, 0x5a, 0x7c, 0xa3, 0xc9, 0x4e, 0x1b, 
    0x45, 0xe5, 0xc0, 0x29, 0x9a
]

key = [
    0x7b, 0x2e, 0xf1, 0xeb, 0x8b, 0x76, 0xe7, 0x68, 0x77, 0xa3, 0xef, 0x52, 0xf6, 
    0x3c, 0xda, 0xaa, 0xf6, 0xa7, 0x43, 0xeb, 0x21, 0x24, 0xc3, 0x9c, 0x7d, 0x08, 
    0x33, 0xb7, 0xf7, 0x2c, 0xb4
]

target_bytes = bytearray(target)
key_bytes = bytearray(key)

flag1 = mode5_reverse(mode3_transform(mode1_reverse(target_bytes)), key_bytes)
flag2 = mode5_reverse(mode1_reverse(mode3_transform(target_bytes)), key_bytes)
flag3 = mode3_transform(mode5_reverse(mode1_reverse(target_bytes), key_bytes))
flag4 = mode3_transform(mode1_reverse(mode5_reverse(target_bytes, key_bytes)))
flag5 = mode1_reverse(mode5_reverse(mode3_transform(target_bytes), key_bytes))
flag6 = mode1_reverse(mode3_transform(mode5_reverse(target_bytes, key_bytes)))

def try_decode(data, name):
    try:
        print(f"{name}: {data.decode('ascii')}")
    except:
        print(f"{name} (binary): {''.join(chr(b) if 32 <= b < 127 else '.' for b in data)}")

print("Possible flag values:")
try_decode(flag1, "Pipeline: Mode 5 -> Mode 3 -> Mode 1")
try_decode(flag2, "Pipeline: Mode 5 -> Mode 1 -> Mode 3")
try_decode(flag3, "Pipeline: Mode 3 -> Mode 5 -> Mode 1")
try_decode(flag4, "Pipeline: Mode 3 -> Mode 1 -> Mode 5")
try_decode(flag5, "Pipeline: Mode 1 -> Mode 5 -> Mode 3")
try_decode(flag6, "Pipeline: Mode 1 -> Mode 3 -> Mode 5")

'''
### Writeup
The challenge involves reversing three transformations applied to an encoded flag:
1. Mode 1: XOR each byte with the previous byte.
2. Mode 3: XOR each byte with 0x56.
3. Mode 5: XOR each byte with a repeating key.

By applying the transformations in reverse order for different possible encoding pipelines, we attempt to recover the correct flag.
'''

# NOTE:
# My script is looking horrible so i asked chatGPT to write better version. (I got not much time left to write this writeup actually :) )
