# Relatively Simple Algorithm

## Description

[RSA](rsa.txt) strikes strikes again again! [Source](rsa.py)

## Solution

In the [rsa.txt](rsa.txt) file also get `p` and `q`, so let's write a siple [script](RelativelySimpleAlgorithm.py) to decrypt the message

```python
totn = (p - 1) * (q - 1)
d = pow(e, -1, totn)

m = pow(c, d, n)
print(binascii.unhexlify(hex(m)[2:]).decode())
```

#### **FLAG >>** `actf{old_but_still_good_well_at_least_until_quantum_computing}`