# I'm so Random 

## Description

Aplet's quirky and unique so he made my own [PRNG](chall.py)! It's not like the other PRNGs, its absolutely unbreakable!

`nc crypto.2021.chall.actf.co 21600`

## Solution

Analyzing the code we see that the random number is calculated as the product of two pseudorandom numbers

This pseudorandom numbers are created from a seed between `10000000` and `99999999` 

Thinking about it, there aren't that many possibilities...so maybe...we can try to brute force it...

First let's generate all of the random numbers (WARNING!! 700MB file)

```python
f = open("random_number", "w")

for seed in range(10000000, 99999999):
    num =int(str(seed**2).rjust(16, "0")[4:12])
    f.write(str(num) + "\n")

f.close()
```

Before submitting our random number prevision we can retrieve from the service 3 already generated random numbers. So we can use them to discard the useless ones from the list of numbers, in order to try to understand which are the two seeds necessary for the generation.

```python
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
```

```console
$ python ImsoRandom.py 
[+] Opening connection to crypto.2021.chall.actf.co on port 21600: Done
[67438321, 26016634]
b"Congrats! Here's your flag: \n"
b'actf{middle_square_method_more_like_middle_fail_method}\n'
```


#### **FLAG >>** `actf{middle_square_method_more_like_middle_fail_method}`