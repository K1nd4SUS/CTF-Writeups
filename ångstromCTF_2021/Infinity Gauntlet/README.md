# Infinity Gauntlet

## Descrizione

All clam needs to do is snap and finite will turn into infinite...

Find it on the shell server at `/problems/2021/infinity_gauntlet` or over netcat at `nc shell.actf.co 21700`.

## Soluzione

In progress...

```python
nc = remote('shell.actf.co', 21700)

nc.recvline()
nc.recvline()

flag = [' '] * 100

def ans(i, q, r):
    if i >= 0x32:
        p = (r >> 8) - i
        c = (r ^ (p * 0x11)) & 255
        log.info(f'flag[{p}] = {chr(c)}')
        flag[p] = chr(c)
        log.info(''.join(flag))
    else:
        log.info(f'Round {i}: {r}')

    nc.sendline(str(r))
    a = nc.recvline().decode().strip()
    if a == 'Wrong!':
        log.failure(f'{q}\t\t{a}')
        exit(1)

for i in range(1, 200):
    r = nc.recvline().decode().strip()
    if not re.fullmatch(r'=== ROUND \d+ ===', r):
        log.failure(f'Unknown line: {r}')
        nc.interactive()
        exit(1)
    
    q = nc.recvline().decode().strip()

    m = re.fullmatch(r'foo\((\d+), (\d+)\) = \?', q)
    if m:
        x = int(m.group(1))
        y = int(m.group(2))
        r = (y + 1) ^ x ^ 1337
        ans(i, q, r)
        continue

    m = re.fullmatch(r'foo\((\d+), \?\) = (\d+)', q)
    if m:
        x = int(m.group(1))
        r = int(m.group(2))
        y = (r ^ x ^ 1337) - 1
        ans(i, q, y)
        continue

    m = re.fullmatch(r'foo\(\?, (\d+)\) = (\d+)', q)
    if m:
        y = int(m.group(1))
        r = int(m.group(2))
        x = (r ^ (y + 1) ^ 1337)
        ans(i, q, x)
        continue
    
    m = re.fullmatch(r'bar\((\d+), (\d+), (\d+)\) = \?', q)
    if m:
        x = int(m.group(1))
        y = int(m.group(2))
        z = int(m.group(3))
        r = (z + 1) * y + x
        ans(i, q, r)
        continue

    m = re.fullmatch(r'bar\((\d+), (\d+), \?\) = (\d+)', q)
    if m:
        x = int(m.group(1))
        y = int(m.group(2))
        r = int(m.group(3))
        z = (r - x) // y - 1
        ans(i, q, z)
        continue
    
    m = re.fullmatch(r'bar\((\d+), \?, (\d+)\) = (\d+)', q)
    if m:
        x = int(m.group(1))
        z = int(m.group(2))
        r = int(m.group(3))
        y = (r - x) // (z + 1)
        ans(i, q, y)
        continue

    m = re.fullmatch(r'bar\(\?, (\d+), (\d+)\) = (\d+)', q)
    if m:
        y = int(m.group(1))
        z = int(m.group(2))
        r = int(m.group(3))
        x = r - (z + 1) * y
        ans(i, q, x)
        continue
```

#### **FLAG >>** `actf{snapped_away_the_end}`