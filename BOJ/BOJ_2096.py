import sys


n = int(sys.stdin.readline())
arr = [[()] * 3 for _ in range(2)]
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split(" ")))
    idx = i % 2
    for j in range(3):
        if i == 0:
            arr[idx][j] = (tmp[j], tmp[j])
        else:
            if j == 0:
                arr[idx][j] = (
                    max(arr[~idx][j][0], arr[~idx][j + 1][0]) + tmp[j],
                    min(arr[~idx][j][1], arr[~idx][j + 1][1]) + tmp[j],
                )
            elif j == 1:
                arr[idx][j] = (
                    max(arr[~idx][j - 1][0], arr[~idx][j][0], arr[~idx][j + 1][0])
                    + tmp[j],
                    min(arr[~idx][j - 1][1], arr[~idx][j][1], arr[~idx][j + 1][1])
                    + tmp[j],
                )
            else:
                arr[idx][j] = (
                    max(arr[~idx][j - 1][0], arr[~idx][j][0]) + tmp[j],
                    min(arr[~idx][j - 1][1], arr[~idx][j][1]) + tmp[j],
                )
val1, val2 = -1, sys.maxsize
for a, b in arr[(n - 1) % 2]:
    val1 = max(val1, a)
    val2 = min(val2, b)
print(val1, val2)
