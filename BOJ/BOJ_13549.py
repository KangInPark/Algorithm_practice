from heapq import heappop, heappush
import sys

n, k = map(int, sys.stdin.readline().split(" "))
q = []
dist = [sys.maxsize] * 100001
chk = [0] * 100001
dist[n] = 0
heappush(q, (0, n))
while q:
    d, curr = heappop(q)
    if chk[curr] == 1:
        continue
    chk[curr] = 1
    adj = [(curr + 1, 1), (curr - 1, 1), (curr * 2, 0)]
    for next, w in adj:
        if next >= 0 and next <= 100000 and d + w < dist[next]:
            dist[next] = d + w
            heappush(q, (dist[next], next))
print(dist[k])
