import time
import random
import os
from pwn import *

f = open("random_number", "w")
for seed in range(10000000, 99999999):
    num =int(str(seed**2).rjust(16, "0")[4:12])
    f.write(str(num) + "\n")
f.close()

num =[]

f = open("random_number", "r")
for x in f:
    num.append(int(x))
f.close()

conn = remote("crypto.2021.chall.actf.co",21600)

conn.recvuntil("Would you like to get a random output [r], or guess the next random number [g]? ")
conn.sendline("r")
num1 = int(conn.recvline().decode('utf-8').strip())

conn.recvuntil("Would you like to get a random output [r], or guess the next random number [g]? ")
conn.sendline("r")
num2 = int(conn.recvline().decode('utf-8').strip())

conn.recvuntil("Would you like to get a random output [r], or guess the next random number [g]? ")
conn.sendline("r")
num3 = int(conn.recvline().decode('utf-8').strip())

list_num_1 = []

for i in num:
    if(i != 0):
        if(num1 % i == 0):
            list_num_1.append(i)

for i in range(len(list_num_1)):
    list_num_1[i] = int(str(list_num_1[i] ** 2).rjust(16, "0")[4:12])

list_num_2 = []

for i in list_num_1:
    if(i != 0):
        if(num2 % i == 0):
            list_num_2.append(i)

for i in range(len(list_num_2)):
    list_num_2[i] = int(str(list_num_2[i] ** 2).rjust(16, "0")[4:12])

list_num_3 = []

for i in list_num_2:
    if(i != 0):
        if(num3 % i == 0):
            list_num_3.append(i)

list_num_3 = list(dict.fromkeys(list_num_3))
print(list_num_3)

conn.recvuntil("Would you like to get a random output [r], or guess the next random number [g]? ")
conn.sendline("g")

conn.recvuntil("What is your guess to the next value generated? ")
for i in range(len(list_num_3)):
    list_num_3[i] = int(str(list_num_3[i] ** 2).rjust(16, "0")[4:12])
conn.sendline(str(list_num_3[0] * list_num_3[1]))

conn.recvuntil("What is your guess to the next value generated? ")
for i in range(len(list_num_3)):
    list_num_3[i] = int(str(list_num_3[i] ** 2).rjust(16, "0")[4:12])
conn.sendline(str(list_num_3[0] * list_num_3[1]))

res = conn.recvline()
print(res)
res = conn.recvline()
print(res)



