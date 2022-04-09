from collections import deque
from sys import maxsize


n, k = map(int, input().split(" "))
q = deque()
chk = [maxsize] * 100001
cnt = [0] * 100001
q.append(n)
chk[n] = 0
cnt[n] = 1

while q:
    curr = q.popleft()
    if curr == k:
        continue
    adj = [curr - 1, curr + 1, curr * 2]
    for next in adj:
        if next >= 0 and next <= 100000:
            if chk[next] > chk[curr] + 1:
                chk[next] = chk[curr] + 1
                cnt[next] = cnt[curr]
                q.append(next)
            elif chk[next] == chk[curr] + 1:
                cnt[next] += cnt[curr]
print(chk[k])
print(cnt[k])
