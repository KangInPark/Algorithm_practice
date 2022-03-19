n, m = map(int, input().split(" "))


def func(arr, idx):
    if len(arr) == m:
        print(" ".join(arr))
        return
    for i in range(idx + 1, n + 1):
        arr.append(str(i))
        func(arr, i)
        arr.pop()


func([], 0)
