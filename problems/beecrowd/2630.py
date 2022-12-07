#!/usr/bin/env python3

# https://www.beecrowd.com.br/judge/en/problems/view/2630

t = int(input())

c = 1
while t:
    t -= 1
    p = input()
    r, g, b = map(int, input().split())

    opts = {
        "eye": lambda r, g, b: int(r * 0.30 + g * 0.59 + b * 0.11),
        "mean": lambda r, g, b: int((r + g + b) / 3),
        "max": lambda r, g, b: max(r, g, b),
        "min": lambda r, g, b: min(r, g, b),
    }

    resolver = opts[p]
    print("Caso #%d: %d" % (c, resolver(r, g, b)))
    c += 1