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


n, e = map(int, sys.stdin.readline().split(" "))
adj = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split(" "))
    adj[a].append((b, c))
    adj[b].append((a, c))
v1, v2 = map(int, sys.stdin.readline().split(" "))
start = dij(1)
mid1 = dij(v1)
mid2 = dij(v2)
ret = min(start[v1] + mid1[v2] + mid2[n], start[v2] + mid2[v1] + mid1[n])
if ret >= sys.maxsize:
    print(-1)
else:
    print(ret)
