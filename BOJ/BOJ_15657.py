def func(idx, cnt, string):
    if cnt == m:
        print(string)
        return
    for i in range(idx, n):
        func(i, cnt + 1, string + arr[i] + " ")


n, m = map(int, input().split(" "))
arr = input().split(" ")
arr.sort(key=lambda x: int(x))
func(0, 0, "")
