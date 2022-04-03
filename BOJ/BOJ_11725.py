import sys


def dfs(curr, chk):
    for next in adj[curr]:
        if chk[next] == 0:
            chk[next] = 1
            arr[next] = curr
            dfs(next, chk)


sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split(" "))
    adj[a].append(b)
    adj[b].append(a)
arr = [0] * (n + 1)
arr[1] = 1
chk = [0] * (n + 1)
chk[1] = 1
dfs(1, chk)
for i in range(2, n + 1):
    print(arr[i])
