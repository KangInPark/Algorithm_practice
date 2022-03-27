from collections import deque
import sys


def bfs():
    q = deque()
    chk = [[[0, 0] for _ in range(m)] for _ in range(n)]
    q.append((0, 0, 0))
    chk[0][0][0] = 1
    chk[0][0][1] = 1
    while q:
        x, y, boom = q.popleft()
        if x == n - 1 and y == m - 1:
            print(chk[x][y][boom])
            return

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if chk[nx][ny][boom] == 0 and arr[nx][ny] == "0":
                    chk[nx][ny][boom] = chk[x][y][boom] + 1
                    q.append((nx, ny, boom))
                elif boom == 0 and arr[nx][ny] == "1" and chk[nx][ny][boom + 1] == 0:
                    chk[nx][ny][boom + 1] = chk[x][y][boom] + 1
                    q.append((nx, ny, boom + 1))
    print(-1)


n, m = map(int, sys.stdin.readline().split(" "))
arr = []
for _ in range(n):
    arr.append(sys.stdin.readline())
bfs()
