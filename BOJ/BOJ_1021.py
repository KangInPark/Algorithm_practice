import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split(" "))
dq = deque([x for x in range(1, n + 1)])
tmp = map(int, sys.stdin.readline().split(" "))
cnt1 = 0
cnt2 = 0
size = n
for val in tmp:
    if dq[0] == val:
        dq.popleft()
        continue
    for i in range(len(dq)):
        if dq[i] == val:
            target = i
            break
    if len(dq) // 2 >= target:
        cnt = 0
        while dq[0] != val:
            dq.append(dq.popleft())
            cnt += 1
        dq.popleft()
        cnt1 += cnt
    else:
        cnt = 0
        while dq[0] != val:
            dq.appendleft(dq.pop())
            cnt += 1
        dq.popleft()
        cnt2 += cnt
print(cnt1 + cnt2)
