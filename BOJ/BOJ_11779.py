from heapq import heappop, heappush
import sys


def dij():
    dist = [sys.maxsize] * (n + 1)
    chk = [0] * (n + 1)
    dist[start] = 0
    q = []
    heappush(q, (0, start, -1))
    while q:
        d, curr, prev = heappop(q)
        if chk[curr] != 0:
            continue
        chk[curr] = prev
        for next, w in adj[curr]:
            if w + d < dist[next]:
                dist[next] = w + d
                heappush(q, (dist[next], next, curr))
    return dist, chk


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split(" "))
    adj[a].append((b, c))
start, end = map(int, sys.stdin.readline().split(" "))
dist, chk = dij()
path = [str(end)]
curr = chk[end]
while curr != -1:
    path.append(str(curr))
    curr = chk[curr]
print(dist[end])
print(len(path))
print(" ".join(path[::-1]))
