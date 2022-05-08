from heapq import heappop, heappush
import math
import sys


def func(adj):
    chk = [0] * n
    q = []
    ret = 0.0
    heappush(q, (0, 0))
    while q:
        d, curr = heappop(q)
        if chk[curr] != 0:
            continue
        chk[curr] = 1
        ret += d
        for next, w in adj[curr]:
            heappush(q, (w, next))
    return ret


n = int(sys.stdin.readline())
adj = [[] for _ in range(n)]
star = []
for _ in range(n):
    a, b = map(float, sys.stdin.readline().split(" "))
    star.append((a, b))
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        dist = math.sqrt(
            (star[i][0] - star[j][0]) ** 2 + (star[i][1] - star[j][1]) ** 2
        )
        adj[i].append((j, dist))
        adj[j].append((i, dist))
ret = func(adj)
print(f"{ret:.2f}")
