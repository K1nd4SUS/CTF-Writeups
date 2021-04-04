import binascii
from pwn import *

conn = remote("crypto.2021.chall.actf.co",21602)
conn.recvuntil("Would you like to encrypt [1], or try encrypting [2]? ")
conn.sendline("1")
conn.recvuntil("What would you like to encrypt: ")
conn.sendline("00000000000000000000000000000000")
zero = binascii.unhexlify(conn.recvline()[:32])
# print(len(zero))
# (zero.hex())

conn.recvuntil("Would you like to encrypt [1], or try encrypting [2]? ")
conn.sendline("1")
conn.recvuntil("What would you like to encrypt: ")
conn.sendline("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
uno = binascii.unhexlify(conn.recvline()[:32])
# print(len(uno))
# print(uno.hex())

zero_bin = bin(int(str("00000000000000000000000000000000"), 16))[2:].zfill(128)
zero_bin_enc = bin(int(str(zero.hex()), 16))[2:].zfill(128)
# print("ZERO   -> " + zero_bin)
# print("ZERO E -> " + zero_bin_enc)

uno_bin = bin(int(str("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"), 16))[2:].zfill(128)
uno_bin_enc = bin(int(str(uno.hex()), 16))[2:].zfill(128)
# print("UNO    -> " + uno_bin)
# print("UNO  E -> " + uno_bin_enc)

conn.recvuntil("Would you like to encrypt [1], or try encrypting [2]? ")
conn.sendline("2")

for k in range(10):
    flag = conn.recvline().decode('utf-8').strip()
    flag = flag.replace("Encrypt this: ", "")
    print(flag + " - " + str(len(flag)))


    flag_enc = ""

    flag_bin = bin(int(str(flag[0:32]), 16))[2:].zfill(128)
    # print(len(flag_bin))
    print(flag_bin)

    for i in range(128):
        if(flag_bin[i] == "0"):
            flag_enc += zero_bin_enc[i]
        if(flag_bin[i] == "1"):
            flag_enc += uno_bin_enc[i]

    flag_bin = bin(int(str(flag[32:64]), 16))[2:].zfill(128)
    # print(len(flag_bin))
    print(flag_bin)

    for i in range(128):
        if(flag_bin[i] == "0"):
            flag_enc += zero_bin_enc[i]
        if(flag_bin[i] == "1"):
            flag_enc += uno_bin_enc[i]

    # print(flag_enc)

    to_send = hex(int(flag_enc, 2))[2:]
    # print("SEND -> " + to_send)
    conn.sendline(str(to_send))


res = conn.recvline()
print(res)
res = conn.recvline()
print(res)