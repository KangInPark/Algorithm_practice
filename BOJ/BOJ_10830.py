import sys


n, b = map(int, sys.stdin.readline().split(" "))
mat = []
for _ in range(n):
    mat.append(list(map(int, sys.stdin.readline().split(" "))))


def matmul(A, B):
    ret = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ret[i][j] += (A[i][k] * B[k][j]) % 1000
            ret[i][j] %= 1000
    return ret


def matpow(A, m):
    if m == 1:
        return A
    if m % 2 == 0:
        tmp = matpow(A, m // 2)
        return matmul(tmp, tmp)
    else:
        tmp = matpow(A, m - 1)
        return matmul(A, tmp)


def func(x):
    return str(x % 1000)


ret = matpow(mat, b)
for i in range(len(ret)):
    print(" ".join(map(func, ret[i])))
