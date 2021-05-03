# nooombers

## Description 

I really do not understand what this is about, but my cousin told me that once he managed to got a flag out of this. I was able to copy from my cousin's shell parts of his interactions with the server. You can find them in interaction1.txt and interaction2.txt. Unfortunately, they are incomplete.

`nooombers.challenges.ooo 8765`

[interaction1.txt](interaction1.txt) f6aeae3c35be2f8a2d098d076e4bf7ac9f5ece24ddc88c9e7fb43016e049b89a

[interaction2.txt](interaction2.txt) 6fd5facfefdbd20b82d651520edf56713ef585bad1b78788db06c4208d2da321

## Solution

First of all let's try to connect to the service

```console
$ nc nooombers.challenges.ooo 8765
Welcome to nooombers! Press enter to start...

騇騇騇
魽
鯌
鬏
魖
魓
鬇
鯽
鬑
鯦
魹
魧
騇
```

Let's try to analyze the files that are given to us 

```
髛髛髛
鬆
魢
魀
鯞
鮂
魻
鬼
鮳
鯑
鮽
魵
髛 鬆
鬆 鱷鳘鰬鰛鳘鰑鳌鲯鳗鲳鱃鰢鲣鲴鲌鰊鲤鲜鰩鰽鱡鱒鳮鳖鰹鱖鳃鱘鰑鰊鰄鰆鱉鳼鱨鳢鱑鲀鲒鳆鰢鲔鰕鳤鳾鲳鲜鲉鱚鳞鲑鱔鳽鱄鳪鲥鰻鳲鲷鲉鱍鲚鲻鱲鰩鲜鰨鰶鰛鱪鱔鱭鳹鳤鳘鲻鱬鲈鲼鲭鲨鳨鱎鳯鳕鰷鲓鰣鲺鲜鳖鱻鱌鰫鱶鲓鰴鳶鳙鱽鳰鲼鲒鲵鱜鱸鰄鱒鰻鱱鲊鳧鲔鰢鰛鰲鳛鲵鲯鱤鰺鰮鱷鰐鱠鲓鲯鲷鲯鲙鳥鱝鰸鰚鱈鲒鲲鱱鳣鰂鳇鲫鳃鳾
髛髛髛
鬆
魢
魀
鯞
鮂
魻
鬼
鮳
鯑
鮽
魵
髛 魢
髛 鱷鳘鰬鰛鳘鰑鳌鲯鳗鲳鱃鰢鲣鲴鲌鰊鲤鲜鰩鰽鱡鱒鳮鳖鰹鱖鳃鱘鰑鰊鰄鰆鱉鳼鱨鳢鱑鲀鲒鳆鰢鲔鰕鳤鳾鲳鲜鲉鱚鳞鲑鱔鳽鱄鳪鲥鰻鳲鲷鲉鱍鲚鲻鱲鰩鲜鰨鰶鰛鱪鱔鱭鳹鳤鳘鲻鱬鲈鲼鲭鲨鳨鱎鳯鳕鰷鲓鰣鲺鲜鳖鱻鱌鰫鱶鲓鰴鳶鳙鱽鳰鲼鲒鲵鱜鱸鰄鱒鰻鱱鲊鳧鲔鰢鰛鰲鳛鲵鲯鱤鰺鰮鱷鰐鱠鲓鲯鲷鲯鲙鳥鱝鰸鰚鱈鲒鲲鱱鳣鰂鳇鲫鳃鳾
魢 鱷鳘鰬鰛鳘鰑鳌鲯鳗鲳鱃鰢鲣鲴鲌鰊鲤鲜鰩鰽鱡鱒鳮鳖鰹鱖鳃鱘鰑鰊鰄鰆鱉鳼鱨鳢鱑鲀鲒鳆鰢鲔鰕鳤鳾鲳鲜鲉鱚鳞鲑鱔鳽鱄鳪鲥鰻鳲鲷鲉鱍鲚鲻鱲鰩鲜鰨鰶鰛鱪鱔鱭鳹鳤鳘鲻鱬鲈鲼鲭鲨鳨鱎鳯鳕鰷鲓鰣鲺鲜鳖鱻鱌鰫鱶鲓鰴鳶鳙鱽鳰鲼鲒鲵鱜鱸鰄鱒鰻鱱鲊鳧鲔鰢鰛鰲鳛鲵鲯鱤鰺鰮鱷鰐鱠鲓鲯鲷鲯鲙鳥鱝鰸鰚鱈鲒鲲鱱鳣鰂鳇鲫鳃鳾 鲛鱾鳅鰩鲽鰨鲖鰿鱏鲽鰋鲆鳸鱲鲽鰜鱓鳼鲫鲚鲅鰍鰽鲃鱪鳉鰮鰐鰡鰌鰗鲡鰚鲻鱢鰴鲘鰋鳢鱮鲛鳧鳜鱶鰽鰵鳽鱢鲃鱔鰗鳆鲒鰰鳨鰼鰰鳈鱢鳌鲥鲡鲊鱞鰺鳘鱘鲵鲹鳒鳙鰬鳭鳜鲬鲦鰀鱬鰾鰆鳩鳱鰯鳸鰙鲾鲚鲖鲝鱍鱥鲑鰅鱥鰗鰣鱑鳜鳹鱑鱴鱈鱌鲒鱾鳝鱼鱈鰴鲱鰒鲜鱊鱛鲂鲙鱷鰹鲉鲥鳞鰐鰠鱩鱹鳒鳁鳞鱧鰟鰫鳋鱙鱱鱯鱸鰌鰻鱑鳨鱷鰶鱒鲯 鳺鰕鳝鰬鳃鲕鳒鱝鱒鰔鲬鰅鳳鰘鰸鳖鰎鱡鰚鳷鳶鱬鲍鲷鲾鲈鱎鳼鳟鰟鲗鲬鳃鲒鰰鱺鲂鲠鳟鳆鱉鳰鰰鱢鰔鰣鳰鲬鳒鰭鳺鲷鲷鲰鳗鳞鲮鰐鲎鳑鱭鰼鱧鳓鰳鰱鱢鰖鳵鱾鳬鳣鱫鰞鰅鲙鰅鲋鰃鲵鳫鲑鳍鱕鰨鰧鳼鳞鱑鰛鳮鱢鳑鰟鱏鲌鱍鲤鲾鳣鳄鰊鱆鱑鰉鱕鱈鱔鱴鰴鱞鳨鱃鱱鱧鰈鳴鱍鰨鳅鲦鳇鲨鳍鲒鱷鲋鲉鰀鰋鰟鱌鳟鲐鲞鲴鱱鲕鱝鱙鳟鰡鲸鰽
髛髛髛
鬆
魢
魀
鯞
鮂
魻
鬼
鮳
鯑
鮽
魵
髛 鯞
髛 鱷鳘鰬鰛鳘鰑鳌鲯鳗鲳鱃鰢鲣鲴鲌鰊鲤鲜鰩鰽鱡鱒鳮鳖鰹鱖鳃鱘鰑鰊鰄鰆鱉鳼鱨鳢鱑鲀鲒鳆鰢鲔鰕鳤鳾鲳鲜鲉鱚鳞鲑鱔鳽鱄鳪鲥鰻鳲鲷鲉鱍鲚鲻鱲鰩鲜鰨鰶鰛鱪鱔鱭鳹鳤鳘鲻鱬鲈鲼鲭鲨鳨鱎鳯鳕鰷鲓鰣鲺鲜鳖鱻鱌鰫鱶鲓鰴鳶鳙鱽鳰鲼鲒鲵鱜鱸鰄鱒鰻鱱鲊鳧鲔鰢鰛鰲鳛鲵鲯鱤鰺鰮鱷鰐鱠鲓鲯鲷鲯鲙鳥鱝鰸鰚鱈鲒鲲鱱鳣鰂鳇鲫鳃鳾
髛 鳺鰕鳝鰬鳃鲕鳒鱝鱒鰔鲬鰅鳳鰘鰸鳖鰎鱡鰚鳷鳶鱬鲍鲷鲾鲈鱎鳼鳟鰟鲗鲬鳃鲒鰰鱺鲂鲠鳟鳆鱉鳰鰰鱢鰔鰣鳰鲬鳒鰭鳺鲷鲷鲰鳗鳞鲮鰐鲎鳑鱭鰼鱧鳓鰳鰱鱢鰖鳵鱾鳬鳣鱫鰞鰅鲙鰅鲋鰃鲵鳫鲑鳍鱕鰨鰧鳼鳞鱑鰛鳮鱢鳑鰟鱏鲌鱍鲤鲾鳣鳄鰊鱆鱑鰉鱕鱈鱔鱴鰴鱞鳨鱃鱱鱧鰈鳴鱍鰨鳅鲦鳇鲨鳍鲒鱷鲋鲉鰀鰋鰟鱌鳟鲐鲞鲴鱱鲕鱝鱙鳟鰡鲸鰽
鯞 鱷鳘鰬鰛鳘鰑鳌鲯鳗鲳鱃鰢鲣鲴鲌鰊鲤鲜鰩鰽鱡鱒鳮鳖鰹鱖鳃鱘鰑鰊鰄鰆鱉鳼鱨鳢鱑鲀鲒鳆鰢鲔鰕鳤鳾鲳鲜鲉鱚鳞鲑鱔鳽鱄鳪鲥鰻鳲鲷鲉鱍鲚鲻鱲鰩鲜鰨鰶鰛鱪鱔鱭鳹鳤鳘鲻鱬鲈鲼鲭鲨鳨鱎鳯鳕鰷鲓鰣鲺鲜鳖鱻鱌鰫鱶鲓鰴鳶鳙鱽鳰鲼鲒鲵鱜鱸鰄鱒鰻鱱鲊鳧鲔鰢鰛鰲鳛鲵鲯鱤鰺鰮鱷鰐鱠鲓鲯鲷鲯鲙鳥鱝鰸鰚鱈鲒鲲鱱鳣鰂鳇鲫鳃鳾 鳺鰕鳝鰬鳃鲕鳒鱝鱒鰔鲬鰅鳳鰘鰸鳖鰎鱡鰚鳷鳶鱬鲍鲷鲾鲈鱎鳼鳟鰟鲗鲬鳃鲒鰰鱺鲂鲠鳟鳆鱉鳰鰰鱢鰔鰣鳰鲬鳒鰭鳺鲷鲷鲰鳗鳞鲮鰐鲎鳑鱭鰼鱧鳓鰳鰱鱢鰖鳵鱾鳬鳣鱫鰞鰅鲙鰅鲋鰃鲵鳫鲑鳍鱕鰨鰧鳼鳞鱑鰛鳮鱢鳑鰟鱏鲌鱍鲤鲾鳣鳄鰊鱆鱑鰉鱕鱈鱔鱴鰴鱞鳨鱃鱱鱧鰈鳴鱍鰨鳅鲦鳇鲨鳍鲒鱷鲋鲉鰀鰋鰟鱌鳟鲐鲞鲴鱱鲕鱝鱙鳟鰡鲸鰽 鲛鱾鳅鰩鲽鰨鲖鰿鱏鲽鰋鲆鳸鱲鲽鰜鱓鳼鲫鲚鲅鰍鰽鲃鱪鳉鰮鰐鰡鰌鰗鲡鰚鲻鱢鰴鲘鰋鳢鱮鲛鳧鳜鱶鰽鰵鳽鱢鲃鱔鰗鳆鲒鰰鳨鰼鰰鳈鱢鳌鲥鲡鲊鱞鰺鳘鱘鲵鲹鳒鳙鰬鳭鳜鲬鲦鰀鱬鰾鰆鳩鳱鰯鳸鰙鲾鲚鲖鲝鱍鱥鲑鰅鱥鰗鰣鱑鳜鳹鱑鱴鱈鱌鲒鱾鳝鱼鱈鰴鲱鰒鲜鱊鱛鲂鲙鱷鰹鲉鲥鳞鰐鰠鱩鱹鳒鳁鳞鱧鰟鰫鳋鱙鱱鱯鱸鰌鰻鱑鳨鱷鰶鱒鲯 鱲鱆鰵鱒鰫鱣鰦鱸鱾鰈鲠鰯鰌鱋鰿鲲鰢鳦鰑鲡鰋鲿鲁鲳鰆鰵鳊鰒鳓鲪鱰鰪鳚鱪鱌鰻鰙鱤鰱鳌鳈鰇鰐鰑鳑鰾鲉鳗鲱鱹鱩鱿鲂鰱鱫鳺鰰鲠鰻鳎鱢鳩鳸鲃鲃鰹鲍鲊鳠鰏鰆鱀鱞鱰鳲鲄鰘鰸鳑鰼鲣鰳鳃鰹鰩鱽鱂鳠鳼鰩鳆鰅鲎鳹鰵鱾鲑鱭鰉鱐鱋鰠鳙鰞鲍鰁鱛鰉鲁鱗鳆鳽鰒鲅鱼鳯鳾鳩鲄鱶鰹鳱鲜鱗鳙鰬鱋鳂鳹鳇鳻鱹鱀鱿鳥鲎鲜鱴鰐鱙鰵鱧鳟鰢
```

Work with these symbols is not the best, let's converts the strings in something more readable

```
Welcome to nooombers! Press enter to start...

INIT
0
1
2
3
4
5
6
7
8
9
10
I 0
0 sequenza 1
INIT
0
1
2
3
4
5
6
7
8
9
10
I 1
I sequenza 1
1 sequenza 1 sequenza 2 sequenza 3
INIT
0
1
2
3
4
5
6
7
8
9
10
I 3
I sequenza 1
I sequenza 3
3 sequenza 1 sequenza 3 sequenza 2 sequenza 4
INIT
0
1
2
3
4
5
6
7
8
9
10
I 2
I sequenza 1
2 sequenza 1 sequenza 2 sequenza 5
INIT
0
1
2
3
4
5
6
7
8
9
10
I 4
I sequenza 1
I sequenza 5
4 sequenza 1 sequenza 5 sequenza 2 sequenza 6
INIT
0
1
2
3
4
5
6
7
8
9
10
I 3
I sequenza 4
I sequenza 6
3 sequenza 4 sequenza 6 sequenza 2 sequenza 6
INIT
0
1
2
3
4
5
6
7
8
9
10
I 3
I sequenza 6
I sequenza 6
3 sequenza 6 sequenza 6 sequenza 2 sequenza 7
INIT
0
1
2
3
4
5
6
7
8
9
10
I 3
I sequenza 7
I sequenza 6
3 sequenza 7 sequenza 6 sequenza 2 sequenza 8
INIT
0
1
2
3
4
5
6
7
8
9
10
I 3
I sequenza 8
I sequenza 6
3 sequenza 8 sequenza 6 sequenza 2 sequenza 9
INIT
0
1
2
3
4
5
6
7
8
9
10
I 3
I sequenza 9
I sequenza 6
3 sequenza 9 sequenza 6 sequenza 2 sequenza 10
INIT
0
1
2
3
4
5
6
7
8
9
10
I 3
I sequenza 10
I sequenza 6
3 sequenza 10 sequenza 6 sequenza 2 sequenza 11
INIT
0
1
2
3
4
5
6
7
8
9
10
I 3
I sequenza 11
I sequenza 6
3 sequenza 11 sequenza 6 sequenza 2 sequenza 12
INIT
0
1
2
3
4
5
6
7
8
9
10
I 3
I sequenza 12
I sequenza 6
3 sequenza 12 sequenza 6 sequenza 2 sequenza 13
INIT
0
1
2
3
4
5
6
7
8
9
10
I 3
I sequenza 13
I sequenza 6
3 sequenza 13 sequenza 6 sequenza 2 sequenza 14
Too much! Disabling one option...
INIT
0
1
2
3
4
5
6
7
8
10
I 4
I sequenza 7
I sequenza 8
4 sequenza 7 sequenza 8 sequenza 2 sequenza 11
INIT
0
1
2
3
4
5
6
7
8
10
I 6
I sequenza 8
I sequenza 7
```

So, we have some sort of menu

The user can choose a command between 0 and 10 and after that, based on the command, a sequence or more are requested as input and as result some sequences are given in output

In the other file we found this (always converted to something more readable)

```
INIT
0
1
2
3
4
5
6
7
8
9
10
I 9
I A
I B
2 B C D
4 E D C F
4 A D C G
6 H F I J
6 K G I L
5 J L I M
0 N
1 N C O
3 M N C P
3 P O C A
9 E A B A
Correct signature! This is the flag:
```

So the option `9` seems the one to get the flag, and based on the other file we can make only a limited number of rounds

Let's try to recreate the [first file interaction](interaction1.txt)

```python
from pwn import *

def ricevi():
    temp = conn.recvline()
    temp = temp.strip()
    temp = temp.split(b" ")
    return temp

def invio(elem):
    conn.recvuntil(i + b" ")
    conn.sendline(elem)

conn = remote("nooombers.challenges.ooo",8765)

conn.recvuntil("Welcome to nooombers! Press enter to start...")
conn.sendline("")
conn.recvline()
init = conn.recvline()

i = init[:3]
log.info(f"I > {i}")

menu = []
for k in range(0, 11):
    menu.append("")

sequenza = []
for k in range(0, 15):
    sequenza.append("")

for k in range(len(menu)):
    menu[k] = conn.recvline().strip()

invio(menu[0])
temp = ricevi()
sequenza[1] = temp[1]

invio(menu[1])
invio(sequenza[1])
temp = ricevi()
sequenza[2] = temp[2]
sequenza[3] = temp[3]

invio(menu[3])
invio(sequenza[1])
invio(sequenza[3])
temp = ricevi()
sequenza[4] = temp[4]

invio(menu[2])
invio(sequenza[1])
temp = ricevi()
sequenza[5] = temp[3]

invio(menu[4])
invio(sequenza[1])
invio(sequenza[5])
temp = ricevi()
sequenza[6] = temp[4]

invio(menu[3])
invio(sequenza[4])
invio(sequenza[6])
temp = ricevi()

invio(menu[3])
invio(sequenza[6])
invio(sequenza[6])
temp = ricevi()
sequenza[7] = temp[4]

invio(menu[3])
invio(sequenza[7])
invio(sequenza[6])
temp = ricevi()
sequenza[8] = temp[4]

invio(menu[3])
invio(sequenza[8])
invio(sequenza[6])
temp = ricevi()
sequenza[9] = temp[4]

invio(menu[3])
invio(sequenza[9])
invio(sequenza[6])
temp = ricevi()
sequenza[10] = temp[4]

invio(menu[3])
invio(sequenza[10])
invio(sequenza[6])
temp = ricevi()
sequenza[11] = temp[4]

invio(menu[3])
invio(sequenza[11])
invio(sequenza[6])
temp = ricevi()
sequenza[12] = temp[4]

invio(menu[3])
invio(sequenza[12])
invio(sequenza[6])
temp = ricevi()
sequenza[13] = temp[4]

invio(menu[3])
invio(sequenza[13])
invio(sequenza[6])
temp = ricevi()
sequenza[14] = temp[4]

#print('\n'.join('{}: {}'.format(*k) for k in enumerate(sequenza)))

for i in range(1, len(sequenza)):
    print(f"{i} -> {sequenza[i].decode('utf-8')}")
print(conn.recvline().decode())
```

```
1 -> 鳃鰜鲣鰨鳰鳃鲩鰇鱰鲧鳷鱶鱠鳏鱈鰂鳏鱞鲠鳜鰙鱇鱄鲓鲡鰣鳵鱫鰣鳩鳗鰄鰂鲓鲗鳎鲘鱮鰋鱾鱬鰀鱴鲯鰓鲦鰣鳈鰮鳙鱇鰄鱬鰣鱦鲃鰝鳥鲕鰣鲸鰂鲐鲲鱥鰽鰜鲞鲂鱗鰛鰕鳸鱧鲘鱐鱸鳦鱿鱝鳏鳢鳍鲮鳏鱀鱙鳡鱏鱦鱀鰦鲄鱥鳂鱁鳛鱞鱬鱬鲟鳫鲯鰦鳈鳭鱙鳥鳴鳷鱏鳗鰣鲖鲑鲼鳛鱡鱢鰷鳠鲘鳩鲨鱖鲭鳊鰷鰩鱍鱼鲲鱏鲖鲰鱥鲄鱬鰮鰦鰄鲿鲯鱖
2 -> 鰦鰩鳁鲯鰋鳦鳹鱁鱪鲻鱨鳜鲲鲋鳒鳉鲩鱍鰼鱝鰼鳕鰥鳸鳬鳵鲋鱶鳉鳊鰎鰀鳷鱱鳔鲜鰢鲖鱙鱺鳏鰛鱛鲚鱙鰉鳘鰤鲘鳼鰈鰺鱮鰼鱜鰟鲮鱀鲻鲅鰝鳦鰯鳼鳺鰻鱦鰐鲬鱨鳟鳭鰽鳍鲣鳊鲏鱭鰊鰱鲁鰳鳎鰔鳐鳡鳊鲁鲹鲝鳨鰑鱚鱮鰻鲸鲵鳯鳒鰞鲍鱼鳆鱷鳤鱯鳦鲊鲉鲀鱀鲐鳏鰩鱑鰻鳁鲑鰥鱰鲢鱼鰃鰻鰀鰈鱮鰩鳘鳕鲁鲒鰫鳓鲉鳞鱵鲟鳫鱤鲤鲫鲊鰯
3 -> 鱜鳨鲄鰣鱞鰓鲯鰢鲢鰶鰊鰎鲌鲔鰤鱑鱸鳐鳔鳎鳪鰢鰟鳏鲷鰘鰽鲆鰦鱶鲹鳬鱻鱏鱤鲩鲲鲛鳆鳲鱆鲫鲟鰆鲹鲘鱾鱍鱫鱥鳂鰞鱀鱟鱸鰾鲪鰽鲟鱑鳬鰡鱣鰠鳰鳉鲫鳼鱗鰳鱧鱾鱌鳴鳳鰛鱀鰧鰨鳊鲶鰈鳎鱧鲆鰅鳸鱔鱁鲡鰬鰲鲟鳵鲉鲤鱥鳲鱲鰻鳴鳸鲷鳗鱛鲐鳎鲟鳵鰑鱗鳐鱦鳀鳦鲔鲨鰴鰉鳕鲯鰩鰂鰳鱐鳉鲨鲲鱅鲿鲭鲐鰜鰶鳍鳿鱬鱫鳝鰵鲐鳄鲒鱗
4 -> 鲡鳗鲁鲙鰧鲜鳜鲐鱿鱰鱒鳻鲯鳓鰕鱓鱎鲊鳝鰜鲐鳺鰷鱻鲋鲳鱢鰌鱮鳞鲽鳪鱚鱒鳴鳄鰥鳏鳣鳿鲢鳑鲤鱥鳧鰻鲌鲰鲓鰝鳑鱢鰔鳴鲌鳲鰒鰁鱽鱻鰯鳿鱝鲊鱫鰶鱚鳚鱆鱰鳨鳩鲠鲏鰈鱽鲍鳸鰓鳖鳂鳶鰌鰬鰽鲦鰭鲶鳮鱷鳞鳼鳪鳡鰐鳙鱯鰿鱺鳏鲏鰉鲦鳚鲄鲿鲃鱗鲐鱾鰥鱀鳐鳑鳁鱠鰘鳏鱥鱔鲍鳩鳠鰪鱨鳦鱙鲤鳡鱔鰆鰯鱊鰷鱈鳮鱊鰯鱗鳱鳢鱭鲲鰞
5 -> 鳜鰚鳯鲩鰭鱳鱿鰈鲇鳮鳞鱶鳯鲧鱿鳛鰓鱝鰾鳮鱳鱄鱤鳖鱓鱱鰽鰩鱾鱫鳁鱽鰁鲵鰍鲋鲬鳻鱦鰔鰻鰚鳶鰿鳞鰸鳤鳲鲘鳕鳓鲰鳧鱟鱌鱦鲔鰶鰳鲛鱇鲬鲾鲟鱘鰝鰺鰂鳚鰺鱮鰙鳯鳜鲯鳽鱃鳝鱄鰵鰍鰄鲹鲺鲯鱰鲲鳤鳉鰊鱫鲩鰄鰉鳉鰹鱬鱳鰜鲲鰴鱮鱣鲖鱟鳲鰪鲅鰌鱠鰆鰑鱳鳦鱞鲥鲅鱴鲻鳭鲫鲞鲶鱿鳒鰍鱹鲛鳽鲄鰟鲎鰘鰔鱤鳵鳄鱍鱪鲟鰼鰆鲋鲶
6 -> 鲐鱰鰓鳀鰭鰥鲋鳢鱗鳣鳱鰺鱹鱎鰯鰪鰄鲓鰠鱺鳷鲈鳶鱒鳑鲲鱋鲁鳢鲵鲃鳸鰟鰂鱪鱝鲧鳷鱻鲨鰨鰓鱝鰢鰘鰕鳜鰞鰤鳒鰰鰖鲾鰘鰧鰃鳃鲃鰲鱵鳿鳧鱯鰺鰃鲦鱔鱼鲻鱕鱣鲉鰥鳉鲸鳽鰟鳤鰆鳞鰂鰉鳈鰂鰫鲨鳿鰳鲭鰀鰙鳶鳢鲣鱘鲍鰁鲪鰔鳼鱒鳍鳙鰆鰱鲈鳹鱸鳁鳏鰪鲗鰷鱐鰗鲆鲰鰙鱖鳭鳨鳲鲂鱀鳢鲾鳗鰹鰄鲙鲞鲳鳬鰷鲾鳔鲘鱆鰀鱋鰶鰨鱉鱪
7 -> 鱠鳵鰹鲯鰛鲖鲹鳤鲏鰅鱾鲫鲋鲅鱜鳣鰒鳋鰸鱮鱓鳖鲫鲫鰧鰲鲷鲉鱬鲄鱝鰪鰀鱆鰆鱫鱰鲈鱗鱎鳟鲦鰯鳡鲇鳪鲄鳎鲂鱑鱅鰉鲤鰣鲉鰃鰔鳣鱖鲂鱣鳝鲽鲡鳕鳘鳉鳗鰌鲎鱡鳣鲗鲕鱇鱳鰮鲲鲦鲪鰼鱠鱶鰒鰰鱴鳍鳘鲢鰜鰨鰸鰐鲺鳅鳦鳨鰋鱣鰯鲻鳲鲟鲛鳌鲰鳞鳽鰻鰬鱖鱯鱣鳒鱻鲠鳟鱉鱳鰷鳉鳓鳸鳎鳑鳱鱂鲫鲶鲶鱧鳎鳖鲃鰇鳳鲶鱇鱼鱅鱰鲰鰧鲨
8 -> 鱻鰽鱘鲨鲃鱳鱊鲣鲶鳮鳐鲑鱈鱿鳵鲟鳦鳡鳜鲝鲨鲄鲥鲵鳹鳽鱻鳠鳀鲦鲊鲡鰗鰻鲽鰊鲂鱰鲆鰠鱴鰖鲘鱛鳮鳳鳸鰐鱩鲦鱝鳲鲺鱍鲧鳡鲯鲌鱩鲌鰚鱦鱿鲱鲾鲯鳙鳆鱶鳫鱛鳐鲉鱈鰋鳲鲪鱈鱰鲌鳮鲆鲘鰚鱖鳽鲙鲟鳨鱾鳩鳕鰣鱲鲙鲜鲬鱟鱋鱦鲽鲞鳳鰴鲴鱇鲆鰑鲢鳃鰔鲾鳥鲶鳜鱎鱭鲇鱠鳄鰯鱹鲪鰋鲻鱕鲱鳄鳈鰄鲊鳻鱳鳕鰨鲽鳴鳰鰿鳳鳟鳯鳯鲷
9 -> 鰧鲰鱧鱛鰈鱶鳡鲢鳞鰹鰆鱴鰑鳦鰆鳖鳟鲠鰥鳘鲇鱄鰅鰍鲑鳯鲹鳍鰻鱾鱕鲿鳉鳨鰺鰫鱙鲤鳆鲉鰯鱕鱹鱕鳈鲬鱱鰨鲦鰕鱎鳈鱙鲑鲋鳈鱞鲉鰭鰐鲅鲎鲘鳸鲳鲗鰔鱻鳺鲦鲤鰠鲴鳜鳄鱝鲎鳫鲋鳟鱴鰉鳖鲛鲿鲬鱁鰣鰊鳂鰾鲤鰨鳙鱟鲉鰱鰔鲘鰔鲠鱙鱌鱊鳛鳐鰮鳈鱧鳤鲐鳍鳌鱌鱧鰋鱄鰏鲦鱍鱬鰄鲻鳚鳁鱇鳺鰿鲄鱳鰣鱋鲜鲁鱟鳡鳄鰓鳧鲿鳍鱆鳛鰔
10 -> 鳈鰆鲨鰑鳤鲚鱐鱤鰤鱍鲅鲟鲿鳾鱁鲺鰬鲈鲘鰩鳁鲭鱡鰲鳒鳞鳊鲊鱿鰘鱥鳳鲆鳝鲌鱁鰄鲾鱻鳿鳖鳛鳦鰙鰒鳠鲍鲜鳪鰩鰡鱶鳁鰂鱚鲴鱉鰳鱈鳤鳽鱭鳿鰝鰄鲴鳼鲄鳠鳘鲜鲚鰬鰌鱁鳔鱴鳲鱕鱘鱘鲋鰳鰷鳽鲪鲗鱶鳥鰞鰢鲮鰈鳛鰬鳙鲾鰾鰺鳚鱆鳔鳭鲒鰤鲈鱐鱵鱱鲉鲃鰞鳗鰫鱫鲐鰷鱎鰠鲻鳺鱒鳡鲕鲫鲏鲾鳘鲔鲠鲆鳞鱾鳣鳒鱊鳸鳸鲟鳛鰖鰀鳝鱠
11 -> 鲰鱑鰔鱳鱴鲂鲘鳿鱯鲝鰭鳥鱉鲇鲒鰞鱝鰡鲁鲲鰺鲮鲑鱉鳙鲫鰣鳽鰘鰚鱷鲰鰋鳷鳞鳫鳦鲬鰮鳲鲣鱚鳼鱵鳅鲯鲖鰣鲣鱞鳧鱀鰎鱟鱫鰝鱑鰳鳏鲆鱪鳖鳈鲏鲐鳿鰵鲒鳭鱸鰳鳳鱈鰗鱚鳵鳤鰇鳓鲔鰦鲧鱹鲑鱙鱱鱵鰝鱀鰡鱇鰸鰨鳊鳦鱮鱯鰠鲘鲿鰒鱵鰳鱌鰪鱑鳣鲻鳦鲀鱁鲚鲼鳧鳄鱘鳀鱤鳅鰸鰁鲼鱙鱿鳙鲍鳽鰰鲩鰕鰤鱫鲻鱽鱁鲬鳝鲞鲨鱞鱊鳲鳒鲗
12 -> 鱶鲑鳵鰹鳀鲝鰔鲆鱋鱎鲿鲲鰷鱾鳿鳊鰴鳻鲣鲏鱊鲹鲟鲛鰥鳊鳒鳰鳼鲜鲖鱞鲣鰢鱅鱲鲕鲇鰛鲁鱫鲇鲴鰖鲶鳌鳸鰴鰱鱺鰘鰺鱲鰈鲠鳔鱬鰪鱫鰐鳙鱅鰓鳁鱉鳴鰘鰉鲒鰪鱆鳉鰦鱿鲨鱧鳓鰯鳭鳘鲗鰗鲼鰈鰶鱭鱢鱔鰋鰟鰼鳓鰔鳢鰖鳱鲧鳘鰾鲚鱼鱈鰸鲇鳙鱬鳕鱓鲟鳡鱯鳟鰝鲖鰔鲔鲀鱆鳑鳙鱣鳨鲐鱑鳻鰍鰙鱮鳯鱫鰍鱚鰷鳲鲬鳔鱱鳠鱠鲟鱭鲐鰼鳢
13 -> 鲨鰈鱎鲏鰍鳂鱄鰼鱳鱢鳰鰔鳈鲮鲯鳸鰮鲻鲬鰔鳗鰂鳴鳹鱦鱛鳘鱶鳱鰶鲠鰂鲑鰉鰚鲫鳂鳾鰃鲨鲊鲏鰵鲃鲠鱳鳬鰮鱅鲱鰏鲒鳳鰡鰫鲠鲬鰕鰯鰬鳉鳓鱲鳟鳷鲓鰉鲂鲛鱷鱿鳶鳕鱫鲙鲿鰻鲿鲚鱡鱯鱓鲔鱀鳼鱓鰣鰽鱮鰉鲽鳉鲝鰷鱍鲀鰽鲺鳸鲵鲳鳇鱻鰈鰺鰔鰘鲱鱪鱏鲻鰷鲹鰂鱾鲚鱸鲈鳆鳨鱹鳌鲑鰇鲆鱣鱃鳜鲙鰜鰇鳱鰅鳟鰑鱾鳰鲷鰼鲍鱄鲖鲲鳉
14 -> 鰢鱈鰖鲵鰹鳣鱟鳙鳳鳞鲄鰭鳙鰗鱪鳟鰶鱞鲞鰗鱣鳸鰱鱘鱒鰎鱩鳻鱪鲔鰑鱀鱄鰤鳲鳗鲶鱥鰦鰺鳼鳧鳐鰮鱚鳑鰝鰯鲞鰠鳤鲵鲪鰶鳺鱗鳰鱚鰊鳅鱞鰫鳇鳽鳄鱤鳈鰵鲸鳒鱒鰭鰣鰍鱫鲩鱹鰅鳗鲁鱟鳶鱓鰏鳸鰍鲬鱹鰆鱷鰏鳸鰪鳻鱀鲪鰉鲿鲱鲚鰴鰵鳓鱠鲈鳺鰼鳸鲾鱨鱩鳭鰕鲿鲜鱌鳭鲮鲫鳈鰥鳷鳰鱽鳎鲜鱊鱰鲖鰑鲦鱿鳑鲵鰗鱑鳬鲔鳓鱶鰤鱊鳦鲕
Too much! Disabling one option...
```

In these way we get 14 sequences, `Too much! Disabling one option...` and the option `9` is disabled

So probably we need to use the option `9` in the last iteraction 

From the [interaction2.txt](interaction2.txt) we can see that there are 16 differen sequences, so two are missing, but we can try to do something with what we have

The option `9` require 2 sequences in input and because we have 14 different possibilities we can try them all and see if there are 2 of them that are the solution

```python
from pwn import *

def ricevi():
    temp = conn.recvline()
    temp = temp.strip()
    temp = temp.split(b" ")
    return temp

def invio(elem):
    conn.recvuntil(i + b" ")
    conn.sendline(elem)

for m in range(1, 14):
    for n in range(1, 14):
        log.info(str(f"Tentativo -> {m}-{n}"))
        conn = remote("nooombers.challenges.ooo",8765)

        conn.recvuntil("Welcome to nooombers! Press enter to start...")
        conn.sendline("")
        conn.recvline()
        init = conn.recvline()

        i = init[:3]

        menu = []
        for k in range(0, 11):
            menu.append("")

        sequenza = []
        for k in range(0, 15):
            sequenza.append("")

        for k in range(len(menu)):
            menu[k] = conn.recvline().strip()

        invio(menu[0])
        temp = ricevi()
        sequenza[1] = temp[1]

        invio(menu[1])
        invio(sequenza[1])
        temp = ricevi()
        sequenza[2] = temp[2]
        sequenza[3] = temp[3]

        invio(menu[3])
        invio(sequenza[1])
        invio(sequenza[3])
        temp = ricevi()
        sequenza[4] = temp[4]

        invio(menu[2])
        invio(sequenza[1])
        temp = ricevi()
        sequenza[5] = temp[3]

        invio(menu[4])
        invio(sequenza[1])
        invio(sequenza[5])
        temp = ricevi()
        sequenza[6] = temp[4]

        invio(menu[3])
        invio(sequenza[4])
        invio(sequenza[6])
        temp = ricevi()

        invio(menu[3])
        invio(sequenza[6])
        invio(sequenza[6])
        temp = ricevi()
        sequenza[7] = temp[4]

        invio(menu[3])
        invio(sequenza[7])
        invio(sequenza[6])
        temp = ricevi()
        sequenza[8] = temp[4]

        invio(menu[3])
        invio(sequenza[8])
        invio(sequenza[6])
        temp = ricevi()
        sequenza[9] = temp[4]

        invio(menu[3])
        invio(sequenza[9])
        invio(sequenza[6])
        temp = ricevi()
        sequenza[10] = temp[4]

        invio(menu[3])
        invio(sequenza[10])
        invio(sequenza[6])
        temp = ricevi()
        sequenza[11] = temp[4]

        invio(menu[3])
        invio(sequenza[11])
        invio(sequenza[6])
        temp = ricevi()
        sequenza[12] = temp[4]

        invio(menu[3])
        invio(sequenza[12])
        invio(sequenza[6])
        temp = ricevi()
        sequenza[13] = temp[4]

        invio(menu[9])
        try:
            invio(sequenza[m])
            invio(sequenza[n])
            conn.recvline()
            conn.recvline()
            conn.recvline()
            conn.recvline()
            conn.recvline()
            conn.recvline()
            conn.recvline()
            conn.recvline()
            conn.recvline()
            conn.recvline()
            conn.recvline()
            temp = conn.recvline().decode()
        except:
            log.warn("Errore")
        if "flag" in temp:
            log.success(temp)
            log.success(conn.recvline().decode())
            exit()
        else:
            log.warn(temp)
        conn.close()
```

```console
[*] Tentativo -> 6-2
[+] Opening connection to nooombers.challenges.ooo on port 8765: Done
[+] Correct signature! This is the flag:
[+] OOO{D0Y0uUnd3rstandWh4tANumberIs?}
```

#### **FLAG >>** `OOO{D0Y0uUnd3rstandWh4tANumberIs?}`