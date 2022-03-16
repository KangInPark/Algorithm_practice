import sys


class disj:
    def __init__(self, n):
        self.arr = [x for x in range(n + 1)]
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.arr[x] == x:
            return x
        else:
            self.arr[x] = self.find(self.arr[x])
            return self.arr[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            self.arr[x] = y
        else:
            self.arr[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


n, m = map(int, sys.stdin.readline().split(" "))
s = disj(n)
tlist = list(map(int, sys.stdin.readline().split(" ")))
for i in range(1, len(tlist)):
    if i == 1:
        s.union(0, tlist[i])
    else:
        s.union(tlist[1], tlist[i])
party = []
for j in range(m):
    party.append(list(map(int, sys.stdin.readline().split(" "))))
    for i in range(2, len(party[j])):
        s.union(party[j][1], party[j][i])
val = s.find(0)
ret = 0
for i in range(m):
    if s.find(party[i][1]) != val:
        ret += 1
print(ret)
