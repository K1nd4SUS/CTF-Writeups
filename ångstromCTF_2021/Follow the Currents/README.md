# Follow the Currents

## Description

go with the [flow](enc)... [Source](source.py)

## Solution

The encryption is based on one XOR only and we can reuse the `keystream` function. The only thing missing is the key but because it consists of only 2 bytes we can brute force it

Let's use this simple [script](FollowtheCurrents.py)

```python
import os
import zlib


def keystream(chiave):
	key = bytes(chiave)
	index = 0
	while 1:
		index+=1
		if index >= len(key):
			key += zlib.crc32(key).to_bytes(4,'big')
		yield key[index]

key = [0,0]

with open("enc","rb") as f:
    enc = f.read()

for i in range(256):
    key[0] = i
    for j in range(256):
        key[1] = j
        ciphertext = []
        k = keystream(key)
        for i in enc:
            ciphertext.append(i ^ next(k))
        if(b'actf' in bytes(ciphertext)):
            print(bytes(ciphertext))
```

#### **FLAG >>** `actf{low_entropy_keystream}`