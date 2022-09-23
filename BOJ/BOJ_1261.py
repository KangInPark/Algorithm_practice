import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split(" "))
arr = []
for i in range(m):
    arr.append(list(sys.stdin.readline().strip()))
dq = deque()
dq.append((0, 0, 0))
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
chk = [[0] * n for i in range(m)]
while dq:
    x, y, cnt = dq.popleft()
    if x == m - 1 and y == n - 1:
        print(cnt)
        break
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if nx >= 0 and ny >= 0 and nx < m and ny < n and chk[nx][ny] == 0:
            if arr[nx][ny] == "0":
                dq.appendleft((nx, ny, cnt))
            else:
                dq.append((nx, ny, cnt + 1))
            chk[nx][ny] = 1
