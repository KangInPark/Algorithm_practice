import sys

sys.setrecursionlimit(10**6)


def func(curr, memo):
    if memo[curr] == -1:
        memo[curr] = 0
        for prev in adj[curr]:
            memo[curr] = max(func(prev, memo), memo[curr])
        memo[curr] += data[curr - 1]
    return memo[curr]


t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split(" "))
    data = list(map(int, sys.stdin.readline().split(" ")))
    adj = [[] for _ in range(n + 1)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split(" "))
        adj[y].append(x)
    goal = int(sys.stdin.readline())
    memo = [-1] * (n + 1)
    print(func(goal, memo))
