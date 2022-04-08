from bisect import bisect_left
import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split(" ")))
arr = []
ret1 = []
ret2 = []
for val in data:
    if not arr or arr[-1] < val:
        arr.append(val)
    else:
        arr[bisect_left(arr, val)] = val
    ret1.append(len(arr))

arr = []
for val in data[::-1]:
    if not arr or arr[-1] < val:
        arr.append(val)
    else:
        arr[bisect_left(arr, val)] = val
    ret2.append(len(arr))
ret2.reverse()
answer = -1
for i in range(n):
    answer = max(answer, ret1[i] + ret2[i] - 1)
print(answer)
