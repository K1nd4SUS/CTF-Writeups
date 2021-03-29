from pwn import *
import binascii

conn = remote("mercury.picoctf.net",58913)
conn.recvuntil("What data would you like to encrypt? ")
conn.sendline("A"*49968)
conn.recvuntil("Here ya go!\n")
p = conn.recvline()
conn.recvuntil("What data would you like to encrypt? ")
enc_flag = binascii.unhexlify("51124f4d194969633e4b52026f4c07513a6f4d05516e1e50536c4954066a1c57")
conn.sendline(enc_flag)
conn.recvuntil("Here ya go!\n")
flag = conn.recvline()

print(binascii.unhexlify(flag[:64]))


