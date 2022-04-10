import sys


def power(x, n):
    if n == 1:
        return x % 1000000007
    if n % 2 == 0:
        tmp = power(x, n // 2)
        return (tmp * tmp) % 1000000007
    else:
        tmp = power(x, n - 1)
        return (x * tmp) % 1000000007


m = int(sys.stdin.readline())
ret = 0
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split(" "))
    ret += b * power(a, 1000000007 - 2) % 1000000007
print(ret % 1000000007)
