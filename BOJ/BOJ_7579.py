import sys

n, val = map(int, sys.stdin.readline().split(" "))
m = list(map(int, sys.stdin.readline().split(" ")))
c = list(map(int, sys.stdin.readline().split(" ")))
size = sum(c)
arr = [0] * (size + 1)
for i in range(n):
    for j in range(size, c[i] - 1, -1):
        arr[j] = max(arr[j], arr[j - c[i]] + m[i])
for i in range(size + 1):
    if arr[i] >= val:
        print(i)
        break
