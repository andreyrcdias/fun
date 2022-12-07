#!/usr/bin/env python3

# https://www.beecrowd.com.br/judge/en/problems/view/2342

h = int(input())
exp = input()
r = eval(exp)
print("OVERFLOW" if r > h else "OK")
