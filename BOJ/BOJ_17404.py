import sys

n = int(sys.stdin.readline())
data = []
for _ in range(n):
    data.append(tuple(map(int, sys.stdin.readline().split(" "))))
mval = sys.maxsize
arr = [[0] * 3 for _ in range(n)]
arr[0][0] = data[0][0]
arr[0][1] = sys.maxsize
arr[0][2] = sys.maxsize
for i in range(1, n):
    arr[i][0] = min(arr[i - 1][1], arr[i - 1][2]) + data[i][0]
    arr[i][1] = min(arr[i - 1][0], arr[i - 1][2]) + data[i][1]
    arr[i][2] = min(arr[i - 1][0], arr[i - 1][1]) + data[i][2]
mval = min(arr[n - 1][1], arr[n - 1][2])
arr = [[0] * 3 for _ in range(n)]
arr[0][0] = sys.maxsize
arr[0][1] = data[0][1]
arr[0][2] = sys.maxsize
for i in range(1, n):
    arr[i][0] = min(arr[i - 1][1], arr[i - 1][2]) + data[i][0]
    arr[i][1] = min(arr[i - 1][0], arr[i - 1][2]) + data[i][1]
    arr[i][2] = min(arr[i - 1][0], arr[i - 1][1]) + data[i][2]
mval = min(mval, arr[n - 1][0], arr[n - 1][2])
arr = [[0] * 3 for _ in range(n)]
arr[0][0] = sys.maxsize
arr[0][1] = sys.maxsize
arr[0][2] = data[0][2]
for i in range(1, n):
    arr[i][0] = min(arr[i - 1][1], arr[i - 1][2]) + data[i][0]
    arr[i][1] = min(arr[i - 1][0], arr[i - 1][2]) + data[i][1]
    arr[i][2] = min(arr[i - 1][0], arr[i - 1][1]) + data[i][2]
mval = min(mval, arr[n - 1][0], arr[n - 1][1])
print(mval)
