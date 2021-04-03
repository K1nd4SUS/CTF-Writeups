# Exclusive Cipher

## Description

Clam decided to return to classic cryptography and revisit the XOR cipher! Here's some hex encoded ciphertext:

`ae27eb3a148c3cf031079921ea3315cd27eb7d02882bf724169921eb3a469920e07d0b883bf63c018869a5090e8868e331078a68ec2e468c2bf13b1d9a20ea0208882de12e398c2df60211852deb021f823dda35079b2dda25099f35ab7d218227e17d0a982bee7d098368f13503cd27f135039f68e62f1f9d3cea7c`

The key is 5 bytes long and the flag is somewhere in the message.

## Solution

We know that the sequence `actf{` is in the ciphertext, so we can calculate the key base on this and use it to decode the entire string

After this we can delete the first byte from the ciphertext and repeat the step above

So let's write a simple [script](ExclusiveCipher.py)

```python
import binascii

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

c = binascii.unhexlify("ae27eb3a148c3cf031079921ea3315cd27eb7d02882bf724169921eb3a469920e07d0b883bf63c018869a5090e8868e331078a68ec2e468c2bf13b1d9a20ea0208882de12e398c2df60211852deb021f823dda35079b2dda25099f35ab7d218227e17d0a982bee7d098368f13503cd27f135039f68e62f1f9d3cea7c")
# actf{
flag = binascii.unhexlify("616374667b")
key = binascii.unhexlify("")

k = 0

while (k + 5 <= len(c)):
    key = byte_xor(flag, c[k:k+5])
    # print(key)
    m = []
    for i in range(k, len(c), 5):
        m.append(byte_xor(key, c[i:i+5]))
    print(b''.join(m))
    k += 1
```

Now we have all the useful decrypted strings, and if we search we find this

```
b'actf{t8bm`M-p`ka\x1ct`|M4}`aM:zpPz"c`Pj,gx!2\x04zjk2/`fd2,{%{z&5j{z&g%l`:eq`3'
b'actf{:u\x7f}B/grvn\x1ecraB6jr|B8mbMu trMe.pj<=\x06mxv=-wty=.l7fu$"xfu$p7qo8rc}<'
b'actf{who_needs_aes_when_you_have_xor}. Good luck on the other crypto!'
b'actf{jxMsigsaBmgdMjdgyMdcwHz|zgHjr~\x7f92Zcms2qya|2rb"czx,mczx~"t`d|vx3'
b'actf{zZatvqvPpvfZxyv{Zv~fJmngvJ}`cn;%H~|q%cdp~%`\x7f3amj1|amjc3vwvagz$'
```

#### **FLAG >>** `actf{who_needs_aes_when_you_have_xor}`