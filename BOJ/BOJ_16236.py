from collections import deque
import sys

n = int(sys.stdin.readline())
arr = []
x = 0
y = 0
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split(" "))))
    if 9 in arr[i]:
        x = i
        y = arr[i].index(9)

q = deque()
chk = [[0] * n for _ in range(n)]
size = 2
exp = 0
q.append((x, y, 0))
arr[x][y] = 0
ret = 0
chk[x][y] = 1
stack = 0
slist = []
while True:
    if not q and stack != 0:
        slist.sort(key=lambda x: (x[0], x[1]))
        curr = slist[0]
        arr[curr[0]][curr[1]] = 0
        exp += 1
        if exp == size:
            exp = 0
            size += 1
        q.clear()
        chk = [[0] * n for _ in range(n)]
        chk[curr[0]][curr[1]] = 1
        stack = 0
        slist.clear()
        q.append((curr[0], curr[1], curr[2]))
        ret = max(ret, curr[2])
        continue
    elif not q:
        break
    curr = q.popleft()
    if arr[curr[0]][curr[1]] != 0 and arr[curr[0]][curr[1]] < size:
        if stack == 0:
            stack = curr[2]
            slist.append(curr)
            continue
        elif stack == curr[2]:
            slist.append(curr)
            continue
        elif stack < curr[2]:
            slist.sort(key=lambda x: (x[0], x[1]))
            curr = slist[0]
            arr[curr[0]][curr[1]] = 0
            exp += 1
            if exp == size:
                exp = 0
                size += 1
            q.clear()
            chk = [[0] * n for _ in range(n)]
            chk[curr[0]][curr[1]] = 1
            stack = 0
            slist.clear()
            q.append((curr[0], curr[1], curr[2]))
            ret = max(ret, curr[2])
            continue
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    for i in range(4):
        nx = dx[i] + curr[0]
        ny = dy[i] + curr[1]
        if (
            nx >= 0
            and ny >= 0
            and nx < n
            and ny < n
            and chk[nx][ny] == 0
            and arr[nx][ny] <= size
        ):
            chk[nx][ny] = 1
            q.append((nx, ny, curr[2] + 1))
print(ret)
