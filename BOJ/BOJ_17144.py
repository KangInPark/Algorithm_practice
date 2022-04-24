from re import X
import sys


def diffusion(arr):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    add = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j] == -1 or arr[i][j] == 0:
                continue
            else:
                tmp = arr[i][j] // 5
                for idx in range(4):
                    nx = dx[idx] + i
                    ny = dy[idx] + j
                    if nx >= 0 and ny >= 0 and nx < r and ny < c and arr[nx][ny] != -1:
                        add[nx][ny] += tmp
                        add[i][j] -= tmp
    for i in range(r):
        for j in range(c):
            arr[i][j] += add[i][j]


def rotate(arr, pos):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    idx = 0
    x = pos - 1
    y = 0
    while True:
        nx = x + dx[idx]
        ny = y + dy[idx]
        if nx < 0 or ny < 0 or nx > pos or ny >= c:
            idx += 1
            continue
        elif nx == pos and ny == 0:
            arr[x][y] = 0
            break
        arr[x][y] = arr[nx][ny]
        x = nx
        y = ny
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    idx = 0
    x = pos + 2
    y = 0
    while True:
        nx = x + dx[idx]
        ny = y + dy[idx]
        if nx < pos + 1 or ny < 0 or nx >= r or ny >= c:
            idx += 1
            continue
        elif nx == pos + 1 and ny == 0:
            arr[x][y] = 0
            break
        arr[x][y] = arr[nx][ny]
        x = nx
        y = ny


r, c, t = map(int, sys.stdin.readline().split(" "))
arr = []
for _ in range(r):
    arr.append(list(map(int, sys.stdin.readline().split(" "))))
for i in range(r):
    if arr[i][0] == -1:
        pos = i
        break
for _ in range(t):
    diffusion(arr)
    rotate(arr, pos)
ret = 0
for a in arr:
    for val in a:
        if val != -1:
            ret += val
print(ret)
