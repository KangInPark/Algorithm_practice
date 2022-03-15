import sys

block = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (1, 0), (0, 1), (0, 2)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (-1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, -1)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (-1, 1), (-1, 2)],
    [(0, 0), (1, 0), (1, -1), (2, -1)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (1, -1)],
    [(0, 0), (0, 1), (0, 2), (-1, 1)],
    [(0, 0), (1, 0), (2, 0), (1, 1)],
]


def chk(x, y, i):
    for dx, dy in block[i]:
        nx = dx + x
        ny = dy + y
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            return False
    return True


n, m = map(int, sys.stdin.readline().split(" "))
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split(" "))))

ret = -1
for k in range(len(block)):
    for i in range(n):
        for j in range(m):
            if chk(i, j, k):
                ret = max(
                    ret,
                    arr[i + block[k][0][0]][j + block[k][0][1]]
                    + arr[i + block[k][1][0]][j + block[k][1][1]]
                    + arr[i + block[k][2][0]][j + block[k][2][1]]
                    + arr[i + block[k][3][0]][j + block[k][3][1]],
                )
print(ret)
