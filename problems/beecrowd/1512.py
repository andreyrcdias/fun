#!/usr/bin/env python3

# https://www.beecrowd.com.br/judge/en/problems/view/1512

from math import gcd

while True:
    n, a, b = map(int, input().split())
    if n == a == b == 0:
        break
    lcm = (a * b) // gcd(a, b)
    t = n // a + n // b - n // lcm
    print(t)
