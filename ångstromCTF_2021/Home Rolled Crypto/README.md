# Home Rolled Crypto

## Description

Aplet made his own block cipher! Can you break it?

`nc crypto.2021.chall.actf.co 21602`

[Source](chall.py)

## Solution 

Analyzing the code we can see that the encryption is based on ECB, and the only things that the `__block_encrypt` function does is to make bitwise AND and a XOR

To get to the flag we have to encrypt 10 sequences that are given to us

Since the service allows us to encrypt any text we choose, we can use it to encrypt two useful sequences. The first consists of all 1's in binary and the second of all 0's in binary

Now we can use these two cipher sequences to encrypt the text to win 

Let's write some [code](HomeRolledCrypto.py)

```python
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
```

Sometimes the encryption fails, but you can still get the flag by trying again to start the code 


#### **FLAG >>** `actf{no_bit_shuffling_is_trivial}`