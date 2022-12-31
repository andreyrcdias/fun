n, x = map(int, input().split())
arr = list(map(int, input().split()))

def find_sum(n, x, arr):
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == x:
                return f"{i+1} {j+1}"
    return "IMPOSSIBLE"

print(find_sum(n, x, arr))

