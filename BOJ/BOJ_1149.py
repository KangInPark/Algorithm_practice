import sys


n = int(sys.stdin.readline())
arr = [[sys.maxsize] * 3 for _ in range(n)]
for i in range(n):
    r, g, b = map(int, sys.stdin.readline().split(" "))
    if i == 0:
        arr[0] = [r, g, b]
    else:
        arr[i][0] = min(arr[i - 1][1] + r, arr[i - 1][2] + r)
        arr[i][1] = min(arr[i - 1][0] + g, arr[i - 1][2] + g)
        arr[i][2] = min(arr[i - 1][0] + b, arr[i - 1][1] + b)
print(min(arr[n - 1]))
