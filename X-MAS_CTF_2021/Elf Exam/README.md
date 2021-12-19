# Elf Exam

## Description

Every year before Christmas, the elves are put to the test. Usually the questions on the test are pretty simple, but this year Santa wanted to mess up with the elves so he gave them only one really hard question:

Given two integers N and M, construct a matrix of size NxM which respect the following proprieties:

- No two elements in the matrix are the same (i.e. mat[i][j] != mat[k][l] if and only if i != k or j != l)
- Any two neighbouring elements in the matrix differ by exactly one bit. two elements in the matrix are neighbouring if they are adjacent (i.e. the neighbours of (i, j) are {(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)}).
- The maximal value in the matrix is minimal

Since Santa realised that the matrices are very big and he doesn't have time to check the whole matrix for each elf, he only wants one line with index P and one column with index Q from this matrix.

Restrictions and Clarifications:

- 2 <= N, M <= 1024
- 0 <= P < N and 0 <= Q < M (the matrix is 0-indexed)
- Note that you don't have to minimize the values on the line P and column Q, you have to minimize the maximal value from the matrix regardless of P and Q
- If there are multiple solutions that respect the conditions above, any will be considered correct.

Example:

(N, M) = (3, 3)

(P, Q) = (1, 2)

Desired output:

Line P = [1, 0, 2]

Column Q = [6, 2, 10]

Explanation:

One of the valid matrices of size 3x3 is:

[[5 4 6],

[1 0 2],

[9 8 10]]

The line with index 1 is [1, 0, 2] and the column with index 2 is [6, 2, 10].

`nc challs.xmas.htsp.ro 5007`

## Solution

```python
#!/usr/bin/env python3

from pwn import *
from collections import deque

def gray(N):
    if N == 0:
        return []
    if N == 1:
        return [0]
    
    b = N.bit_length()
    p = 1 << (b - 1)

    S = deque(i ^ (i >> 1) for i in reversed(range(p)))
    if N % p == 0:
        return S

    S2 = gray(N % p)

    S.rotate(-(S.index(S2[0]) + 1))
    S.extend(x + p for x in S2)

    return S

nc = remote('challs.xmas.htsp.ro', 5007)

for _ in range(25):
    nc.recvuntil(b'Step: ')
    print(nc.recvlineS().strip())
    
    nc.recvuntil(b'(N, M) = ')
    N, M = eval(nc.recvlineS().strip())
    
    nc.recvuntil(b'(P, Q) = ')
    P, Q = eval(nc.recvlineS().strip())

    BN = bin(N - 1)[2:] + '~'
    BM = bin(M - 1)[2:] + '~'

    TN = [0] * (len(BN) - 1)
    TM = [0] * (len(BM) - 1)

    i, j = 0, 0
    for k in range(len(TN) + len(TM) - 1, -1, -1):
        if BN[i:] < BM[j:]:
            i += 1
            TN[-i] = k
        else:
            j += 1
            TM[-j] = k

    GN = gray(N)
    GM = gray(M)

    def get(i, j):
        x = 0
        for k in range(len(TN)):
            if GN[i] & 1 << k:
                x |= 1 << TN[k]
        for k in range(len(TM)):
            if GM[j] & 1 << k:
                x |= 1 << TM[k]
        return x

    LP = [get(P, j) for j in range(M)]
    LQ = [get(i, Q) for i in range(N)]
    
    nc.sendline(str(LP).encode())
    nc.sendline(str(LQ).encode())

print(nc.recvallS(timeout=2))

```

#### **FLAG >>** `X-MAS{Gr4y_C0d35_H4v3_S0_M4ny_Int3rest1n6_Pr0pr13rti3s_h8uef21r}`