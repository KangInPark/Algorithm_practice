from collections import deque


a, b = map(int, input().split(" "))
q = deque()
q.append((a, 1))
ans = -1
while q:
    curr, val = q.popleft()
    if curr == b:
        ans = val
        break
    for next in [curr * 2, curr * 10 + 1]:
        if next <= b:
            q.append((next, val + 1))
print(ans)
