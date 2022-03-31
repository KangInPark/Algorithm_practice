import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
adj = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split(" "))
    adj[a][b] = min(c, adj[a][b])

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                continue
            if adj[i][k] + adj[k][j] < adj[i][j]:
                adj[i][j] = adj[i][k] + adj[k][j]
ret = ""
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if adj[i][j] == sys.maxsize:
            ret += "0 "
        else:
            ret += str(adj[i][j]) + " "
    ret += "\n"
print(ret)
