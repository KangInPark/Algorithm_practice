import sys

n = int(sys.stdin.readline())
arr = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    tmp = list(map(int, sys.stdin.readline().split(" ")))
    for j in range(len(tmp)):
        arr[i][j + 1] = tmp[j]
for i in range(2, n + 1):
    for j in range(1, i + 1):
        if j == i:
            arr[i][j] = arr[i - 1][j - 1] + arr[i][j]
        else:
            arr[i][j] = max(arr[i - 1][j - 1], arr[i - 1][j]) + arr[i][j]
print(max(arr[n]))
