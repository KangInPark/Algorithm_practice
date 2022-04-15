import sys


n, m, r = map(int, sys.stdin.readline().split(" "))
adj = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]
data = list(map(int, sys.stdin.readline().split(" ")))
for _ in range(r):
    a, b, c = map(int, sys.stdin.readline().split(" "))
    adj[a][b] = c
    adj[b][a] = c

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                adj[i][j] = 0
                continue
            if adj[i][k] + adj[k][j] < adj[i][j]:
                adj[i][j] = adj[i][k] + adj[k][j]
ret = -1
for i in range(1, n + 1):
    add = 0
    for j in range(1, n + 1):
        if adj[i][j] <= m:
            add += data[j - 1]
    ret = max(ret, add)
print(ret)
