import sys


def func(chk, cnt, mval, idx):
    if cnt == m:
        ret = 0
        for i in range(len(house)):
            for val in data[i]:
                if chk[val[0]] == 1:
                    ret += val[1]
                    break
        mval[0] = min(ret, mval[0])
        return
    for i in range(idx, len(chick)):
        if chk[i] == 0:
            chk[i] = 1
            func(chk, cnt + 1, mval, i + 1)
            chk[i] = 0


n, m = map(int, sys.stdin.readline().split(" "))
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split(" "))))

house = []
chick = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append((i + 1, j + 1))
        elif arr[i][j] == 2:
            chick.append((i + 1, j + 1))
data = [[] for _ in range(len(house))]
for i in range(len(house)):
    for j in range(len(chick)):
        data[i].append(
            (j, abs(chick[j][0] - house[i][0]) + abs(chick[j][1] - house[i][1]))
        )
    data[i].sort(key=lambda x: x[1])
mval = [sys.maxsize]
func([0] * len(chick), 0, mval, 0)
print(mval[0])
