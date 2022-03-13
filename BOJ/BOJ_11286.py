import heapq
import sys

arr = []
n = int(sys.stdin.readline())
ret = ""
for i in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(arr, (abs(x),x))
    else:
        if(arr):
            ret += str(heapq.heappop(arr)[1]) + '\n'
        else:
            ret += "0\n"
print(ret)