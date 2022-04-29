from heapq import heappop, heappush
import sys


def prim():
    chk = [0] * (n + 1)
    q = []
    heappush(q, (0, 1))
    ret = 0
    val = -1

    while q:
        d, curr = heappop(q)
        if chk[curr] == 1:
            continue
        chk[curr] = 1
        ret += d
        val = max(val, d)
        for next, w in adj[curr]:
            if chk[next] == 0:
                heappush(q, (w, next))
    return ret - val


n, m = map(int, sys.stdin.readline().split(" "))
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split(" "))
    adj[a].append((b, c))
    adj[b].append((a, c))
print(prim())
