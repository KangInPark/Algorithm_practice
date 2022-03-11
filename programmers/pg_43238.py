from heapq import *

def solution(n, times):
    hq = []
    val = 0
    arr = [1] * len(times)
    unit = 0.0
    for t in times:
        unit += 1 / t; 
    lb = n * 1/unit
    cnt = 0
    for idx, t in enumerate(times):
        val = int(lb/t)
        arr[idx] += val
        cnt += val
        heappush(hq, (t * arr[idx], idx))
        arr[idx] += 1
    while True:
        val, idx = heappop(hq)
        cnt += 1
        if cnt == n:
            return val
        heappush(hq, (times[idx]*arr[idx], idx))        
        arr[idx] += 1
