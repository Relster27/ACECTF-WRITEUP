#!/usr/bin/env python

with open("Reverseme.png", "rb") as f:
    data = f.read()

with open("reversed.bin", "wb") as f:
    f.write(data[::-1])

# NOTE:
# This is just a pretty simple reverse. Just literally reverse each byte of the binary and output it in an ELF file, and voila flag baby!!
