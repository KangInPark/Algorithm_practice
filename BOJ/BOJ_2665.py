from collections import deque
import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(sys.stdin.readline().strip()))
chk = [[0] * n for _ in range(n)]
dq = deque()
dq.append((0, 0, 0))

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
while dq:
    x, y, cnt = dq.popleft()
    if x == n - 1 and y == n - 1:
        print(cnt)
        break
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if nx >= 0 and ny >= 0 and nx < n and ny < n and chk[nx][ny] == 0:
            if arr[nx][ny] == "1":
                dq.appendleft((nx, ny, cnt))
            else:
                dq.append((nx, ny, cnt + 1))
            chk[nx][ny] = 1
