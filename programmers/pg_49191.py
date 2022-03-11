def dfs(adj, memo, curr, chk):
    if(memo[curr] != -1):
        chk[0] = chk[0] | memo[curr]
        return
    for next in adj[curr]:
        if(chk[0] & 1 << next == 0):
            chk[0] = chk[0] | (1 << next)
            dfs(adj, memo, next, chk)


def solution(n, results):
    adj = [[] for _ in range(n+1)]
    radj = [[] for _ in range(n+1)]
    for x, y in results:
        adj[y].append(x)
        radj[x].append(y)
    memo = [-1] * (n+1)
    rmemo = [-1] * (n+1)
    answer = 0
    chk = [0]
    for i in range(1, n+1):
        chk[0] = 1 << i
        dfs(adj, memo, i, chk)
        memo[i] = chk[0]
        chk[0] = 1 << i
        dfs(radj, rmemo, i, chk)
        rmemo[i] = chk[0]
    for idx in range(1, n+1):
        if bin(memo[idx] | rmemo[idx]).count('1') == n:
            answer += 1
    return answer
