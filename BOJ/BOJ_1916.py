from heapq import heappop, heappush
import sys


def dij(start):
    dist = [sys.maxsize] * (n + 1)
    chk = [False] * (n + 1)
    pq = []
    dist[start] = 0
    heappush(pq, (0, start))
    while pq:
        d, curr = heappop(pq)
        if chk[curr]:
            continue
        chk[curr] = True
        for next, w in adj[curr]:
            if d + w < dist[next]:
                dist[next] = d + w
                heappush(pq, (dist[next], next))
    return dist


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split(" "))
    adj[a].append((b, c))
s, e = map(int, sys.stdin.readline().split(" "))
ret = dij(s)[e]
print(ret)
