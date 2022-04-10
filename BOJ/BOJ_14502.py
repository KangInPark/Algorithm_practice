from collections import deque
from copy import deepcopy
import sys


def func(data):
    q = deque()
    for i in range(n):
        for j in range(m):
            if data[i][j] == 2:
                q.append((i, j))
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while q:
        currx, curry = q.popleft()
        for i in range(4):
            nx = dx[i] + currx
            ny = dy[i] + curry
            if nx >= 0 and ny >= 0 and nx < n and ny < m and data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))


def chk(data):
    func(data)
    ret = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                ret += 1
    return ret


def calc(cnt, val, r):
    if cnt == 3:
        tmp = [item[:] for item in data]
        val[0] = max(val[0], chk(tmp))
        return
    for i in range(r, n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                calc(cnt + 1, val, i)
                data[i][j] = 0


n, m = map(int, sys.stdin.readline().split(" "))
data = []
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split(" "))))
val = [-1]
calc(0, val, 0)
print(val[0])
