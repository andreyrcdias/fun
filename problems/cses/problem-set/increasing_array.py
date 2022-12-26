n = int(input())
arr = list(map(int, input().split()))
total = 0
m = arr[0]
for i in range(1, n):
    total += max(0, m - arr[i])
    m = max(m, arr[i])
print(total)

