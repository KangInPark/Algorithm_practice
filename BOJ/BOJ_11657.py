from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split(" "))
adj = [[] for i in range(n + 1)]
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split(" "))
    adj[a].append((b, c))

dis = [sys.maxsize] * (n + 1)
chk = [0] * (n + 1)
cycle = [0] * (n + 1)
q = deque()
q.append(1)
chk[1] = 1
dis[1] = 0
res = False

while q:
    curr = q.popleft()
    chk[curr] = 0
    cycle[curr] += 1
    if cycle[curr] >= n:
        res = True
        break
    for next, cost in adj[curr]:
        if dis[curr] + cost < dis[next]:
            dis[next] = dis[curr] + cost
            if chk[next] == 0:
                q.append(next)
                chk[next] = 1
if res:
    print(-1)
else:
    for i in range(2, n + 1):
        if dis[i] == sys.maxsize:
            dis[i] = -1
        print(dis[i])
