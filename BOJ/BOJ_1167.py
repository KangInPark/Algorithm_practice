import sys


n = int(sys.stdin.readline())
adj = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    tmp = list(map(int, sys.stdin.readline().split(" ")))
    curr = tmp[0]
    tmp = tmp[1:-1]
    for idx in range(0, len(tmp), 2):
        adj[curr].append((tmp[idx], tmp[idx + 1]))
arr = [0] * (n + 1)
chk = [0] * (n + 1)
answer = [0]


def dfs(idx, answer):
    for child, val in adj[idx]:
        if chk[child] == 0:
            chk[child] = 1
            dfs(child, answer)
            chk[child] = 0
    tmp = []
    for child, val in adj[idx]:
        if chk[child] == 0:
            tmp.append(arr[child] + val)
    if tmp:
        if len(tmp) == 1:
            arr[idx] = tmp[0]
            answer[0] = max(answer[0], tmp[0])
        else:
            tmp.sort(reverse=True)
            arr[idx] = tmp[0]
            answer[0] = max(answer[0], tmp[0] + tmp[1])


chk[1] = 1
dfs(1, answer)
print(answer[0])
