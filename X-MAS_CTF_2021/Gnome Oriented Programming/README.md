# Gnome Oriented Programming 

## Description

A fellow gnome from Santa's toy factory is trying to learn programming to automate his work, he seems to be stuck with something, see if you can help him.

`nc challs.xmas.htsp.ro 1038`

## Solution

Simple one-time-pad

Give the program a text with the lenght of the key, now XOR the result with our input and in this way we get the key.

Now the only things to do is XOR this key with the encrypted flag.

```python
from pwn import *

conn = remote("challs.xmas.htsp.ro",1038)

# Level 1
line1 = conn.recvline().decode('utf-8')
conn.recvuntil(b"Encrypted Flag: ")
flag = eval(conn.recvlineS().strip())

temp = b"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

conn.recvline()
conn.recvuntil(b"input = ")
conn.sendline(temp)

conn.recvuntil(b"Encrypted Input: ")
text = eval(conn.recvlineS().strip())

chiave = xor(temp, text)
print(xor(flag, chiave))
```

```console
$ python crypto.py 
[+] Opening connection to challs.xmas.htsp.ro on port 1038: Done
b'X-MAS{D0n7_Y0u_3v3r_Wr1te_S1n6leton5_F0r_0tp_G3ner4tor5_08hdj12}'
[*] Closed connection to challs.xmas.htsp.ro port 1038
```

#### **FLAG >>** `X-MAS{D0n7_Y0u_3v3r_Wr1te_S1n6leton5_F0r_0tp_G3ner4tor5_08hdj12}`