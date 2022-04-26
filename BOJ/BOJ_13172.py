import sys


def power(x, n):
    if n == 1:
        return x % r
    if n % 2 == 0:
        tmp = power(x, n // 2)
        return (tmp * tmp) % r
    else:
        tmp = power(x, n - 1)
        return (x * tmp) % r


m = int(sys.stdin.readline())
ret = 0
r = 1000000007
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split(" "))
    ret += b * power(a, r - 2) % r
print(ret % r)
