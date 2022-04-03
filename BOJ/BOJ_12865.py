import sys

n, k = map(int, sys.stdin.readline().split(" "))
arr = [0] * (k + 1)
items = []
for _ in range(n):
    w, v = map(int, sys.stdin.readline().split(" "))
    for val in range(k, 0, -1):
        if val >= w:
            arr[val] = max(arr[val - w] + v, arr[val])
print(arr[k])
