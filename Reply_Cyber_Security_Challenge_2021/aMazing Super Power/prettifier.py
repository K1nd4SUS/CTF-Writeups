#!/usr/bin/env python3

edges = []
cities = set()

with open('file.txt') as f:
    for l in f.readlines():
        v, w = l.split('=')
        a, b = map(lambda s: s.replace(' ', '_'), v.split('-'))
        t, e = map(int, w.split(','))

        edges.append((a, b, t, e))
        cities.add(a)
        cities.add(b)

n = len(cities)
cities = list(cities)
index = {c:i for i, c in enumerate(cities)}

mat = [[(10 ** 9, 10 ** 9) for j in range(n)] for i in range(n)]

for a, b, t, e in edges:
    a = index[a]
    b = index[b]
    mat[a][b] = (t, e)

for i in range(n):
    print(cities[i])

for i in range(n):
    for j in range(n):
        print(*mat[i][j], end=' ')
    print()
