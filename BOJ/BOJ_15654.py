n, m = map(int, input().split(" "))

arr = list(map(int, input().split(" ")))
arr.sort()


def func(chk, idx, data):
    if idx == m:
        print(" ".join(data))
        return
    for i in range(n):
        if chk & (1 << i) == 0:
            data.append(str(arr[i]))
            func(chk | (1 << i), idx + 1, data)
            data.pop()


func(0, 0, [])
