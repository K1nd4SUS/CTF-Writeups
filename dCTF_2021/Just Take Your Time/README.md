# Just Take Your Time

## Description

Let's go. In and out. 2 second adventure.

`nc dctf-chall-just-take-your-time.westeurope.azurecontainer.io 9999`

[just-take-your-time.py](just-take-your-time.py)

###### Hint -> While this may not be pwn, its tools may still be quite handy.

## Solution

Analyzig the code we see that the flag is encrypted using the `time()` of the system

```
key = str(int(time())).zfill(16).encode("utf-8")
secret = token_hex(16)
cipher = DES3.new(key, DES3.MODE_CFB, b"00000000")
encrypted = cipher.encrypt(secret.encode("utf-8"))
```

We can connect to the service, pass the first challenge `(a * b)` and get the encrypted secret

Now we can try to decrypt using the time, `-100 / 100` is used to be safer, send it back and get the flag

Let's write the script

```python
from pwn import *
from Crypto.Cipher import DES3
from time import time
from random import randint

nc = remote("dctf-chall-just-take-your-time.westeurope.azurecontainer.io", 9999)

nc.recvline()
a, b = map(int, nc.recvline().decode().strip().split(' ')[::2])
nc.sendline(str(a * b))

t = int(time())
nc.recvline()
secret = bytes.fromhex(nc.recvlineS())
log.info(f"Secret: {secret.hex()}")

for i in range(-100, 100):
    key = str(t + i).zfill(16).encode("utf-8")
    cipher = DES3.new(key, DES3.MODE_CFB, b"00000000")
    plain = cipher.decrypt(secret)
    if plain.isalnum():
        nc.sendline(plain.decode())
        nc.recvline()
        log.info(f"Time: {i}")
        log.success(nc.recvlineS())
        break
```

```console
$ python JustTakeYourTime.py 
[+] Opening connection to dctf-chall-just-take-your-time.westeurope.azurecontainer.io on port 9999: Done
[*] Secret: f24f18b5814062decdb85c6283778d7d2551b62bf039d97dafae5408b6f5b666
[*] Time: -10
[+] dctf{1t_0n1y_t0Ok_2_d4y5...}
```

#### **FLAG >>** `dctf{1t_0n1y_t0Ok_2_d4y5...}`