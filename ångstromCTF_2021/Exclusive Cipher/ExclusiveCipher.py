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
