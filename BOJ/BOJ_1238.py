import sys
import heapq


def dij(x):
    dist = [sys.maxsize] * (n + 1)
    chk = [False] * (n + 1)
    dist[x] = 0
    pq = []
    heapq.heappush(pq, (dist[x], x))
    while pq:
        d, curr = heapq.heappop(pq)
        if chk[curr]:
            continue
        chk[curr] = True
        for next, w in adj[curr]:
            if d + w < dist[next]:
                dist[next] = d + w
                heapq.heappush(pq, (dist[next], next))
    return dist


n, m, x = map(int, sys.stdin.readline().split(" "))
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split(" "))
    adj[a].append((b, c))
ret = dij(x)
answer = -1
for i in range(1, n + 1):
    if i == x:
        continue
    answer = max(answer, dij(i)[x] + ret[i])

print(answer)
