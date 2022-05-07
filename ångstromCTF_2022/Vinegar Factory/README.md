# Vinegar Factory

## Description

Clam managed to get parole for his dumb cryptography jokes, but after making yet another dumb joke on his way out of the courtroom, he was sent straight back in. This time, he was sentenced to 5 years of making dumb Vigenere challenges. Clam, fed up with the monotony of challenge writing, made a program to do it for him. Can you solve enough challenges to get the flag?

Connect to the challenge at `nc challs.actf.co 31333`. [Source](main.py)

## Solution

```python
from turtle import pos
from pwn import *
import string

def extract(res):
    key = ''
    for c, k in zip(res, 'actf'):
        key += string.ascii_lowercase[(string.ascii_lowercase.index(c) - string.ascii_lowercase.index(k)) % len(string.ascii_lowercase)]
    return key

def shift(seq, n):
    a = n % len(seq)
    return seq[-a:] + seq[:-a]

def decrypt(msg, key):
    ret = ""
    i = 0
    for c in msg:
        if c in string.ascii_lowercase:
            ret += string.ascii_lowercase[(string.ascii_lowercase.index(c) - string.ascii_lowercase.index(key[i])) % len(string.ascii_lowercase)]
            i = (i + 1) % len(key)
        else:
            ret += c
    return ret

conn = remote("challs.actf.co",31333)
conn.recvuntil(b"Welcome to the vinegar factory! Solve some crypto, it'll be fun I swear!\n")

for i in range(50):
    print(f"Round[{i}]")
    text = conn.recvline().decode().split(" ")[2]
    conn.recvuntil(b"> ")

    possible_flag = re.findall("[a-z][a-z][a-z][a-z]{[a-z_]{10,50}}[a-z][a-z][a-z][a-z]", text) 

    print(f"Possible flag -> {possible_flag}")

    for res in possible_flag:
        key = extract(res[0:4])

        dec = decrypt(res, key)
        flag = re.findall("actf{[a-z_]{10,50}}fleg", dec) 
        
        if flag:
            print(f"FLAG _> {flag[0].replace('fleg', '')}\n")
            conn.sendline(flag[0].replace("fleg", "").encode())
            break
    else:
        log.error("ERROR")
```

#### **FLAG >>** `actf{classical_crypto_is_not_the_best}`