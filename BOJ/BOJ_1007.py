from math import sqrt
import sys


def func(cnt, idx, sumx, sumy, mval):
    if cnt == n // 2:
        dx = sumx - (tx - sumx)
        dy = sumy - (ty - sumy)
        mval[0] = min(mval[0], sqrt(dx**2 + dy**2))
        return
    if cnt + (n - idx) < n // 2:
        return
    for i in range(idx, n):
        func(cnt + 1, i + 1, sumx + arr[i][0], sumy + arr[i][1], mval)


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    arr = []
    tx = 0
    ty = 0
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split(" "))
        arr.append((x, y))
        tx += x
        ty += y
    mval = [sys.maxsize]
    func(0, 0, 0, 0, mval)
    print("{:.10f}".format(mval[0]))
