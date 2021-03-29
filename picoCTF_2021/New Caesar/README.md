# New Caesar

###### We found a brand new type of encryption, can you break the secret code? (Wrap with picoCTF{}) `lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil` [new_caesar.py](new_caesar.py)

Let's start with analyze [new_caesar.py](new_caesar.py)

The encryption is made in 2 phases
1. b16_encode
2. shift base on the key character

For the decryption we need to apply this 2 phases in reverse order, but we need to invert them. For the shift part a change of sign in the `shift` function is sufficient, while for `b16_encode` we have to write a `b16_decode` function 

```python
def b16_decode(enc):
    list_c = []
    list_bin = []
    plain = ""
    for i in range(0, len(enc), 2):
        list_c.append(enc[i:i+2])
    for i in range(len(list_c)):
        list_bin.append("{0:04b}".format(ALPHABET.find(list_c[i][0])))
        list_bin[i] += str("{0:04b}".format(ALPHABET.find(list_c[i][1])))
    for i in range(len(list_bin)):
        plain += chr(int(list_bin[i], 2))
    return plain

def shift(c, k):
	t1 = ord(c) + LOWERCASE_OFFSET
	t2 = ord(k) + LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]
```

Another thing to do is to find the key, but the length is 1 so we can brute force it

Put all in a [Python script](NewCaesar.py), run and search for the most likely plaintext

#### **FLAG >>** `picoCTF{et_tu?_431db62c5618cd75f1d0b83832b67b46}`

