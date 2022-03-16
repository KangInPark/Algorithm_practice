from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split(" "))
dic = {}
for i in range(n + m):
    x, y = map(int, sys.stdin.readline().split(" "))
    dic[x] = y
q = deque()
chk = [0] * 101
q.append((1, 0))
chk[1] = 1
while q:
    curr = q.popleft()
    if curr[0] == 100:
        print(curr[1])
        break
    for i in range(1, 7):
        nx = curr[0] + i
        if nx <= 100 and chk[nx] == 0:
            chk[nx] = 1
            if nx in dic:
                nx = dic[nx]
            q.append((nx, curr[1] + 1))
