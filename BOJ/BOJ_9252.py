import sys


def func(i, j, ret):
    if i == 0 or j == 0:
        return
    if arr[i - 1][j] == arr[i][j]:
        func(i - 1, j, ret)
    elif arr[i][j - 1] == arr[i][j]:
        func(i, j - 1, ret)
    else:
        ret[0] += A[i - 1]
        func(i - 1, j - 1, ret)


sys.setrecursionlimit(10**6)
A = input()
B = input()

n = len(A)
m = len(B)
arr = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if A[i - 1] == B[j - 1]:
            arr[i][j] = arr[i - 1][j - 1] + 1
        else:
            arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])
ret = [""]
func(n, m, ret)
print(arr[n][m])
print(ret[0][::-1])
