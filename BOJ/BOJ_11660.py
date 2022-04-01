import sys


n, m = map(int, sys.stdin.readline().split(" "))
data = []
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split(" "))))
arr = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if j == 0:
            arr[i][j] = data[i][j]
        else:
            arr[i][j] = arr[i][j - 1] + data[i][j]
for i in range(1, n):
    for j in range(n):
        arr[i][j] += arr[i - 1][j]

for _ in range(m):
    x1, y1, x2, y2 = map(lambda x: int(x) - 1, sys.stdin.readline().split(" "))
    a, b, c = 0, 0, 0
    if x1 != 0:
        a = arr[x1 - 1][y2]
    if y1 != 0:
        b = arr[x2][y1 - 1]
    if x1 != 0 and y1 != 0:
        c = arr[x1 - 1][y1 - 1]
    print(arr[x2][y2] - a - b + c)
