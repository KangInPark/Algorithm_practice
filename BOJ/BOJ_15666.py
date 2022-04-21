import sys


def func(idx, cnt, string, dic, val):
    if cnt == m:
        if string not in dic:
            dic[string] = val[0]
            val[0] += 1
        return
    for i in range(idx, n):
        func(i, cnt + 1, string + arr[i] + " ", dic, val)


n, m = map(int, sys.stdin.readline().split(" "))
arr = sys.stdin.readline().strip().split(" ")
arr.sort(key=lambda x: int(x))
dic = {}
func(0, 0, "", dic, [0])
for item in sorted(list(dic.items()), key=lambda x: x[1]):
    print(item[0])
