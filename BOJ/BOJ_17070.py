import sys


n = int(sys.stdin.readline())
data = []
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split(" "))))
arr = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(3)]  # 0가로 1세로 2대각
arr[0][1][2] = 1
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(3):
            if k == 0 and i == 1 and j == 2:
                continue
            if k == 0:  # 가로
                if data[i - 1][j - 1] == 1 or data[i - 1][j - 2] == 1:
                    continue
                arr[k][i][j] = arr[0][i][j - 1] + arr[2][i][j - 1]
            elif k == 1:  # 세로
                if data[i - 1][j - 1] == 1 or data[i - 2][j - 1] == 1:
                    continue
                arr[k][i][j] = arr[1][i - 1][j] + arr[2][i - 1][j]
            else:  # 대각선
                if (
                    data[i - 1][j - 1] == 1
                    or data[i - 1][j - 2] == 1
                    or data[i - 2][j - 1] == 1
                    or data[i - 2][j - 2] == 1
                ):
                    continue
                arr[k][i][j] = (
                    arr[0][i - 1][j - 1] + arr[1][i - 1][j - 1] + arr[2][i - 1][j - 1]
                )
print(arr[0][n][n] + arr[1][n][n] + arr[2][n][n])
