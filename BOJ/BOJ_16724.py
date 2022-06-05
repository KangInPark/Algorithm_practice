import sys


class disjoint:
    def __init__(self, n):
        self.arr = [i for i in range(n)]

    def find(self, x):
        if self.arr[x] == x:
            return x
        else:
            self.arr[x] = self.find(self.arr[x])
            return self.arr[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.arr[y] = x

    def ret(self):
        s = set()
        for val in self.arr:
            s.add(self.find(val))
        return len(s)


def func(x, y, dj, arr):
    if arr[x][y] == "D":
        nx = x + 1
        ny = y
    elif arr[x][y] == "U":
        nx = x - 1
        ny = y
    elif arr[x][y] == "L":
        nx = x
        ny = y - 1
    elif arr[x][y] == "R":
        nx = x
        ny = y + 1
    arr[x][y] = "X"
    dj.union(x * m + y, nx * m + ny)
    if arr[nx][ny] != "X":
        func(nx, ny, dj, arr)


sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().split(" "))
arr = []
for _ in range(n):
    arr.append(list(sys.stdin.readline()))
dj = disjoint(n * m)
for i in range(n):
    for j in range(m):
        if arr[i][j] != "X":
            func(i, j, dj, arr)
print(dj.ret())
