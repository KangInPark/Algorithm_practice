def matmul(A, B):
    ret = [[0] * len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                ret[i][j] += (A[i][k] * B[k][j]) % 1000000007
            ret[i][j] = ret[i][j] % 1000000007
    return ret


def matpow(A, n):
    if n == 1:
        return A
    if n % 2 == 0:
        tmp = matpow(A, n // 2)
        return matmul(tmp, tmp)
    else:
        tmp = matpow(A, n - 1)
        return matmul(A, tmp)


n = int(input())
A = [[1, 1, 0], [1, 0, 0], [0, 1, 0]]
if n == 0:
    ans = [[0]]
elif n == 1 or n == 2:
    ans = [[1]]
else:
    ans = matmul(matpow(A, n - 2), [[1], [1], [0]])
print(ans[0][0])
