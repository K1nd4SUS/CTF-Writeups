# Easy Peasy

###### A one-time pad is unbreakable, but can you manage to recover the flag? (Wrap with picoCTF{}) nc mercury.picoctf.net 58913 [otp.py](otp.py)

First of all let's try to connect to the service 

```console
$ nc mercury.picoctf.net 58913
******************Welcome to our OTP implementation!******************
This is the encrypted flag!
51124f4d194969633e4b52026f4c07513a6f4d05516e1e50536c4954066a1c57

What data would you like to encrypt?
```

So, it seems like that we have the encrypted flag and we can encrypt whatever we want, but i think is time to look at the [code](otp.py)

When the program starts the flag is encrypted always with the same key and given the result that the function `def startup(key_location):` return, we can assume that the length of the flag is 32 character 

Regarding the other function this are the interesting part

```python
if stop >= KEY_LEN:
		stop = stop % KEY_LEN
		key = kf[start:] + kf[:stop]
```

We know that `KEY_LEN = 50000` so if we encrypt something using all of 50000 characters, the key is being reused from the start

The encryption is based only on XOR, so if we use all 50000 character of the keys, and send back our encrypted flag, we should get the plaintext of it

Because the flag length is 32, we need to send 49968 random characters

Let's do it with a simple [Python script](EasyPeasy.py)

```python
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
```
#### **FLAG >>** `picoCTF{35ecb423b3b43472c35cc2f41011c6d2}`
