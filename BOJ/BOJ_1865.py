from collections import deque
import sys


def spfa(start):
    dist = [sys.maxsize] * (n + 1)
    chk = [False] * (n + 1)
    cnt = [0] * (n + 1)
    q = deque()
    q.append(start)
    dist[start] = 0
    chk[start] = True
    while q:
        curr = q.popleft()
        d = dist[curr]
        chk[curr] = False
        cnt[curr] += 1
        if cnt[curr] == n:
            return True
        for next, w in adj[curr]:
            if d + w < dist[next]:
                dist[next] = d + w
                if not chk[curr]:
                    q.append(next)
    return False


t = int(sys.stdin.readline())
for _ in range(t):
    n, m, w = map(int, sys.stdin.readline().split(" "))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split(" "))
        adj[a].append((b, c))
        adj[b].append((a, c))
    for _ in range(w):
        a, b, c = map(int, sys.stdin.readline().split(" "))
        adj[a].append((b, -c))
    for i in range(1, n + 1):
        adj[0].append((i, 0))
    ret = spfa(0)
    if ret:
        print("YES")
    else:
        print("NO")
