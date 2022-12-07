#!/usr/bin/env python3

# https://www.beecrowd.com.br/judge/en/problems/view/1803

def decode(f, mi, l):
    return (f * mi + l) % 257

def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

m = []
for _ in range(4):
    line = input()
    m.append(list(line))

tm = transpose(m)
f = int("".join(tm.pop(0)))
l = int("".join(tm.pop()))

dm = []
for row in tm:
    mi = int("".join(row))
    dmi = decode(f, mi, l)
    dm.append(dmi)

result = "".join(list(map(chr, dm)))
print(result)
