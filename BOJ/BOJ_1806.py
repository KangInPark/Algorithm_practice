n, s = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
val = 0
idx = 0
ret = 100000000
for i in range(n):
    val += arr[i]
    if val >= s:
        while val >= s:
            ret = min(ret, i - idx + 1)
            val -= arr[idx]
            idx += 1
if ret == 100000000:
    print(0)
else:
    print(ret)
