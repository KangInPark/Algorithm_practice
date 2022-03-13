import sys


n, m = map(int, sys.stdin.readline().split(" "))
inp = list(map(int, sys.stdin.readline().split(" ")))
arr = [0] * (n + 1)
for i in range(1, n + 1):
    arr[i] = arr[i - 1] + inp[i - 1]
for i in range(m):
    x, y = map(int, sys.stdin.readline().split(" "))
    print(arr[y] - arr[x - 1])
