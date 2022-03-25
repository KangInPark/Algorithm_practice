import sys


def dfs(curr, ret):
    ret[0] += chr(curr + ord("A"))
    chk = False
    if adj[curr][0] != -1:
        dfs(adj[curr][0], ret)
    ret[1] += chr(curr + ord("A"))
    if adj[curr][1] != -1:
        dfs(adj[curr][1], ret)
    ret[2] += chr(curr + ord("A"))


n = int(sys.stdin.readline())
adj = [[] for _ in range(n)]
for _ in range(n):
    tmp = list(
        map(
            lambda x: -1 if x == "." else ord(x) - ord("A"),
            sys.stdin.readline().strip().split(" "),
        )
    )
    adj[tmp[0]] = tmp[1:]
ret = ["", "", ""]
dfs(0, ret)
for s in ret:
    print(s)
