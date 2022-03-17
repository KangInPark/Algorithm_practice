cnt = 0


def dfs(x, y, chk, n):
    if x == n - 1:
        global cnt
        cnt += 1
        return
    chk[x] = y
    nx = x + 1
    for ny in range(n):
        tmp = 0
        for i in range(nx):
            if chk[i] == ny or i - nx == chk[i] - ny or i - nx == ny - chk[i]:
                tmp = 1
                break
        if tmp == 0:
            dfs(nx, ny, chk, n)


n = int(input())
for i in range(n):
    dfs(0, i, [-1] * n, n)

print(cnt)
