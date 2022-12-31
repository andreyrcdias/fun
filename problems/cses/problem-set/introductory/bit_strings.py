MOD = 1000000007

n = int(input())

def num_bit_strings(n: int) -> int:
    return pow(2, n, MOD)

print(num_bit_strings(n))

