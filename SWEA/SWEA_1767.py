def func(idx, core, arr, cnt, cost, mval):
    if idx == len(core):
        if mval[0] < cnt:
            mval[0] = cnt
            mval[1] = cost
        elif mval[0] == cnt:
            mval[1] = min(mval[1], cost)
        return
    x, y = core[idx]
    curr = x - 1
    chk = False
    while curr >= 0:
        if arr[curr][y] != 0:
            chk = True
            break
        curr -= 1
    if chk == False:
        curr = x - 1
        while curr >= 0:
            arr[curr][y] = 2
            curr -= 1
        func(idx + 1, core, arr, cnt + 1, cost + x, mval)
        curr = x - 1
        while curr >= 0:
            arr[curr][y] = 0
            curr -= 1

    curr = x + 1
    chk = False
    while curr < n:
        if arr[curr][y] != 0:
            chk = True
            break
        curr += 1
    if chk == False:
        curr = x + 1
        while curr < n:
            arr[curr][y] = 2
            curr += 1
        func(idx + 1, core, arr, cnt + 1, cost + (n - x - 1), mval)
        curr = x + 1
        while curr < n:
            arr[curr][y] = 0
            curr += 1

    curr = y - 1
    chk = False
    while curr >= 0:
        if arr[x][curr] != 0:
            chk = True
            break
        curr -= 1
    if chk == False:
        curr = y - 1
        while curr >= 0:
            arr[x][curr] = 2
            curr -= 1
        func(idx + 1, core, arr, cnt + 1, cost + y, mval)
        curr = y - 1
        while curr >= 0:
            arr[x][curr] = 0
            curr -= 1

    curr = y + 1
    chk = False
    while curr < n:
        if arr[x][curr] != 0:
            chk = True
            break
        curr += 1
    if chk == False:
        curr = y + 1
        while curr < n:
            arr[x][curr] = 2
            curr += 1
        func(idx + 1, core, arr, cnt + 1, cost + (n - y - 1), mval)
        curr = y + 1
        while curr < n:
            arr[x][curr] = 0
            curr += 1

    func(idx + 1, core, arr, cnt, cost, mval)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split(" "))))
    core = []
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if arr[i][j] == 1:
                core.append((i, j))
    mval = [0, 1000]
    func(0, core, arr, 0, 0, mval)
    print(f"#{test_case} {mval[1]}")
    # ///////////////////////////////////////////////////////////////////////////////////
