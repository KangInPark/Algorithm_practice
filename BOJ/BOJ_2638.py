import sys

sys.setrecursionlimit(10**6)


def dfs(x, y):
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if (
            nx >= 0
            and ny >= 0
            and nx < n
            and ny < m
            and chk[nx][ny] == 0
            and data[nx][ny] == 0
        ):
            chk[nx][ny] = 1
            dfs(nx, ny)


def empty():
    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                return False
    return True


n, m = map(int, sys.stdin.readline().split(" "))
data = []
for _ in range(n):
    data.append((list(map(int, sys.stdin.readline().split(" ")))))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
ret = 0
while not empty():
    chk = [[0] * m for _ in range(n)]
    dfs(0, 0)
    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                cnt = 0
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if nx >= 0 and ny >= 0 and nx < n and ny < m and chk[nx][ny] == 1:
                        cnt += 1
                if cnt >= 2:
                    data[i][j] = 0
    ret += 1
print(ret)
