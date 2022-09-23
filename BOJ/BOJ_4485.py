from heapq import heappop, heappush
import sys


def dij(n, arr, pnum):
    dis = [[sys.maxsize] * n for _ in range(n)]
    chk = [[0] * n for _ in range(n)]
    dis[0][0] = arr[0][0]
    q = []
    heappush(q, (dis[0][0], 0, 0))
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while q:
        cnt, x, y = heappop(q)
        if chk[x][y] != 0:
            continue
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            if nx >= 0 and ny >= 0 and nx < n and ny < n:
                if arr[nx][ny] + dis[x][y] < dis[nx][ny]:
                    dis[nx][ny] = arr[nx][ny] + dis[x][y]
                    heappush(q, (dis[nx][ny], nx, ny))
    print(f"Problem {pnum}: {dis[n-1][n-1]}")


pnum = 1
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    arr = []
    for i in range(n):
        arr.append(list(map(int, sys.stdin.readline().split(" "))))

    dij(n, arr, pnum)
    pnum += 1
