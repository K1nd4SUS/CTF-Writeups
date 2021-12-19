# Piano Carol

## Description

Every year on the second day of Christmas, when Santa finally gets some rest, Mrs. Claus plays a carol on her magic piano as a reward for him. The way she plays this carol is quite intriguing.

The piano has N tiles, with a number written on each of the tiles of the piano, that changes from year to year.

Let's call the number on the i-th tile v[i]. When Mrs. Claus presses a tile the piano magically changes the numbers in the follwing way:

If the i-th tile is pressed, both v[i] and v[i + 1] are replaced by the greatest common divisor of v[i] and v[i + 1]. (Note that for some reason, Mrs. Claus can't press the last tile of the piano)

Also, Mrs. Claus can only press a tile if after the press, at least one of the numbers v[i] or v[i + 1] changes it's value.

Now, since Santa is really tired he's gonna fall asleep soon and she wants to play a carol as short as possible. Help her find a list of tile presses with minimal length such that after all the presses, there's no way to do another tile press.

Restrictions and Clarifications:

- It can be prooved that the process of tile pressing is finite
- N <= 2 * 10 ^ 4
- 1 <= v[i] <= 10 ^ 6 for all 1 <= i <= N
- In order to shorten the size of the output, the output should be composed of a series of riffs.(a consecutive list of presses of form x, x+1, x+2, ..., y or x, x-1, x-2, ..., y will be written as (x, y) )
- There's no need to minimize the number of riffs, you need to minimize the number of tiles pressed, and therefore the sum of the lengths of the riffs

Example #1:

N = 5 numbers = [2, 4, 6, 8, 10]

Desired output: Number of riffs: 2

riff #1 (1, 1)

riff #2 (3, 3)

Example #2:

N = 10 numbers = [822877, 374035, 374035, 523649, 109237, 599395, 359637, 239758, 599395, 148987]

Desired output: Number of riffs = 2

riff #1 = (4, 8)

riff #2 = (7, 0)

Explanation for example 1:

- After the first tile press 4 and 6 will be replaced by gcd(4, 6) = 2 so the array of numbers becomes [2, 2, 2, 8, 10].
- After the second tile press the array of numbers becomes [2, 2, 2, 2, 2] and the process is finished.

Explanation for example 2: The expanded tile presses are: 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1, 0
nc challs.xmas.htsp.ro 5009

## Solution

```python
#!/usr/bin/env python3

from pwn import *
from math import gcd

nc = remote('challs.xmas.htsp.ro', 5009)

def solve(num):
    N = len(num)

    sol = (10 ** 9, [])

    for i in range(N):
        g = num[i]
        for j in range(i, N):
            g = gcd(g, num[j])
            if g == 1:
                break
        else:
            continue
        new_sol = (N - i + j - 3, [(i, N - 2), (j - 2, 0)])
        if new_sol[0] < sol[0]:
            sol = new_sol

    return sol

for _ in range(25):
    try:
        nc.recvuntil(b'Step: ')
    except:
        print('Fuck you!')
        break
    
    print(nc.recvlineS().strip())
        
    nc.recvuntil(b'N = ')
    N = int(nc.recvlineS())
    
    nc.recvuntil(b'numbers = ')
    numbers = eval(nc.recvlineS())

    if 1 in numbers:
        assert False, "Not implemented"
    else:
        sol = solve(numbers)[1]

    nc.recvuntil(b'riffs = ')
    nc.sendline(str(len(sol)).encode())
    for r in sol:
        nc.recvuntil(b' = ')
        nc.sendline(str(r).encode())

print(nc.recvallS(timeout=2))
```

#### **FLAG >>** `X-MAS{An0th3r_Gr33dy_4l6or17hm_F0r_Y0ur_H34r7_fo2ibuy4}`