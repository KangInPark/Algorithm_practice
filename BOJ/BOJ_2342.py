import sys


data = list(map(int, sys.stdin.readline().split(" ")))
val = [
    [sys.maxsize, 2, 2, 2, 2],
    [sys.maxsize, 1, 3, 4, 3],
    [sys.maxsize, 3, 1, 3, 4],
    [sys.maxsize, 4, 3, 1, 3],
    [sys.maxsize, 3, 4, 3, 1],
]
n = len(data) - 1
arr = [[[sys.maxsize] * 5 for _ in range(5)] for _ in range(n + 1)]
arr[0][0][0] = 0
for i in range(0, n):
    idx = data[i]
    for j in range(0, 5):
        arr[i + 1][idx][j] = min(
            arr[i][0][j] + val[0][idx],
            arr[i][1][j] + val[1][idx],
            arr[i][2][j] + val[2][idx],
            arr[i][3][j] + val[3][idx],
            arr[i][4][j] + val[4][idx],
        )
    for j in range(0, 5):
        arr[i + 1][j][idx] = min(
            arr[i][j][0] + val[0][idx],
            arr[i][j][1] + val[1][idx],
            arr[i][j][2] + val[2][idx],
            arr[i][j][3] + val[3][idx],
            arr[i][j][4] + val[4][idx],
        )
print(min(map(min, arr[n])))
