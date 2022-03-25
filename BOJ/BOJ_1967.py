import sys


def func(curr, ret):
    tmp = []
    for next, w in adj[curr]:
        func(next, ret)
        tmp.append(arr[next] + w)
    if tmp:
        tmp.append(0)
        tmp.sort(reverse=True)
        arr[curr] = tmp[0]
        ret[0] = max(ret[0], tmp[0] + tmp[1])


n = int(sys.stdin.readline())
adj = [[] * (n + 1) for _ in range(n + 1)]
arr = [0] * (n + 1)
for _ in range(n - 1):
    a, b, c = map(int, sys.stdin.readline().split(" "))
    adj[a].append((b, c))
ret = [0]
func(1, ret)
print(ret[0])
