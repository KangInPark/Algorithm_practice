from bisect import bisect_left
import sys


n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split(" ")))
arr = []
for val in data:
    if not arr:
        arr.append(val)
    elif arr[-1] < val:
        arr.append(val)
    else:
        arr[bisect_left(arr, val)] = val
print(len(arr))
