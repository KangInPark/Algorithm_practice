import sys


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    data = []
    data.append(list(map(int, sys.stdin.readline().split(" "))))
    data.append(list(map(int, sys.stdin.readline().split(" "))))
    arr = [[0] * n for _ in range(2)]
    arr[0][0], arr[1][0] = data[0][0], data[1][0]
    for i in range(1, n):
        if i > 1:
            arr[0][i] = max(arr[1][i - 1] + data[0][i], arr[1][i - 2] + data[0][i])
        else:
            arr[0][i] = arr[1][i - 1] + data[0][i]
        if i > 1:
            arr[1][i] = max(arr[0][i - 1] + data[1][i], arr[0][i - 2] + data[1][i])
        else:
            arr[1][i] = arr[0][i - 1] + data[1][i]
    print(max(arr[0][n - 1], arr[1][n - 1]))
