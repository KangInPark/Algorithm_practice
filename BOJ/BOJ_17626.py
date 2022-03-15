import sys


n = int(input())
arr = [sys.maxsize] * (n + 1)

i = 1
l = []
while True:
    if i * i <= n:
        arr[i * i] = 1
        l.append(i * i)
        i += 1
    else:
        break
for i in range(1, n + 1):
    if arr[i] == 1:
        continue
    for val in l:
        if val > i:
            break
        arr[i] = min(arr[i - val] + 1, arr[i])
print(arr[n])
