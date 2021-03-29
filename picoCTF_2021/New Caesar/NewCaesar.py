import string
ALPHABET = string.ascii_lowercase[:16]
LOWERCASE_OFFSET = ord("a")

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


enc = "lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil"

key = "1"
for k in range(33, 126):
	key = chr(k)
	b16 = ""
	for i, c in enumerate(enc):
		b16 += shift(c, key[i % len(key)])
	print(b16_decode(b16))