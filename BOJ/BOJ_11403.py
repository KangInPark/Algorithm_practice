import sys


def dfs(adj, visited, curr, start):
    for i in range(len(adj)):
        if adj[curr][i] == 1 and visited[start][i] == 0:
            visited[start][i] = 1
            dfs(adj, visited, i, start)


n = int(sys.stdin.readline())
adj = []
for i in range(n):
    adj.append(list(map(int, sys.stdin.readline().split(" "))))
visited = [[0] * n for _ in range(n)]
for i in range(n):
    dfs(adj, visited, i, i)
for arr in visited:
    ret = ""
    for val in arr:
        ret += str(val) + " "
    print(ret.strip())
