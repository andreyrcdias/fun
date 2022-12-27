n = int(input())

if n == 1:
    print(1)
else:
    is_even = lambda n: n % 2 == 0
    while True:
        print(n, end=" ")
        if n == 1:
            break
        if is_even(n):
            n //= 2
        else:
            n *= 3
            n += 1

