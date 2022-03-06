# Class Project 

## Description

I was working on a project for my C programming class and I broke my VM when trying to compile my code! My project is due at 11:59. Can you please help me get my VM up and running again?

VM Password: 1_w1ll_n07_br34k_7h15

https://drive.google.com/drive/folders/1gE4Idj6DjhJ3AX64tOL3Tp31k8gurj94?usp=sharing

## Solution 

The zip contais a `vmdk` files that can be open with VMware

Once started the machine was extremely slow and did not seem to respond even to a simple `ls` in the terminal 

So we opted to stop using this VM and start focusing on the disk content only

We can mount the `vmdk` file into another OS and starting exploring the files

First, let's try to search for `UMDCTF`

```console
$ ack 'UMDCTF'
home/aman_esc/Documents/admin_notes
6:4. UMDCTF Kickoff! - Done!
```

Nice, let's see the content of this file

```console
$ cat admin_notes
ONLY USE THIS ACCOUNT FOR THINGS THAT NEED ESCALATED PRIVS

1. Check homework for today
2. Plan for class tomorrow
3. Remember to hydrate!
4. UMDCTF Kickoff! - Done!
5. Finish paper for English class.
6. Finish project for next Thursday!
7. Verify VU1EQ1RGe2YwcmtfYjBtYjVfNHIzXzRfYjRkXzcxbTN9
```

And here is the flag encoded in `base64`

In the same folder there was also this file

```console
$ cat fork_bomb.bash
#!/bin/bash
:(){ :|:& };:
```

This explain why the VM was so slow...

#### **FLAG >>** `UMDCTF{f0rk_b0mb5_4r3_4_b4d_71m3}`