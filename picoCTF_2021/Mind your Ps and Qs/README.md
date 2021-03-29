# Mind your Ps and Qs

###### In RSA, a small e value can be problematic, but what about N? Can you decrypt this? [values](values)

```
Decrypt my super sick RSA:
c: 843044897663847841476319711639772861390329326681532977209935413827620909782846667
n: 1422450808944701344261903748621562998784243662042303391362692043823716783771691667
e: 65537
```
N in very small, so we can factor it is using [FactorDB](https://factordb.com/)

```
p = 2159947535959146091116171018558446546179
q = 658558036833541874645521278345168572231473
```

Now the only thing that remain to do is decrypt `c`, let's write a simple [Python script](MindyourPsandQs.py) to do it

```python
totn = (p - 1) * (q - 1)
d = pow(e, -1, totn)

m = pow(c, d, n)
print(binascii.unhexlify(str(hex(m))[2:]))
```

#### **FLAG >>** `picoCTF{sma11_N_n0_g0od_00264570}`