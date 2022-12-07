#!/usr/bin/env python3

# https://www.beecrowd.com.br/judge/en/problems/view/3315

weekly_hits = []
for _ in range(4):
    hits = list(map(int, input().split()))
    weekly_hits.append(sum(hits))

m = max(weekly_hits)
b = bin(m).replace("0b", "")
print("%d = %s" % (m, b))
