def func(cnt, string, dic, chk, val):
    if cnt == m:
        if string not in dic:
            dic[string] = val[0]
            val[0] += 1
        return
    for i in range(n):
        if chk[i] == 0:
            chk[i] = 1
            func(cnt + 1, string + arr[i] + " ", dic, chk, val)
            chk[i] = 0


n, m = map(int, input().split(" "))
arr = input().split(" ")
dic = {}
arr.sort(key=lambda x: int(x))
func(0, "", dic, [0] * n, [0])
for item in sorted(list(dic.items()), key=lambda x: x[1]):
    print(item[0])
