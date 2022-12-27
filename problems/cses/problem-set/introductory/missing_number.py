n = int(input())

numbers = list(map(int, input().split()))
numbers = set(sorted(numbers))
expected = set(list(range(1, n)))
missing_numbers = expected - numbers
if missing_numbers:
    print(missing_numbers.pop())
else:
    print(n)

