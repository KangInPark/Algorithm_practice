import sys


def pd(A, B):
    return (A[0] * B[1] - A[1] * B[0]) / 2


n = int(sys.stdin.readline())
start = tuple(map(float, sys.stdin.readline().split(" ")))
sec = tuple(map(float, sys.stdin.readline().split(" ")))
ret = 0.0
for _ in range(n - 2):
    thi = tuple(map(float, sys.stdin.readline().split(" ")))
    ret += pd(
        (sec[0] - start[0], sec[1] - start[1]), (thi[0] - start[0], thi[1] - start[1])
    )
    sec = thi
print(abs(ret))
