from bisect import bisect_left
import sys


n = int(input())
arr = list(map(int, input().split(" ")))
mval = sys.maxsize
ret = []
for i in range(n):
    idx = bisect_left(arr, -arr[i], i + 1, n)
    if idx == n:
        idx -= 1
    for j in range(idx - 1, idx + 2):
        if j == i:
            continue
        if j >= n:
            break
        if abs(arr[j] + arr[i]) < mval:
            mval = abs(arr[j] + arr[i])
            ret = [arr[i], arr[j]]

print(ret[0], ret[1])
