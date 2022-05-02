def func(arr, x, y, chk, boom, cnt, mval):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx >= 0 and nx < n and ny >= 0 and ny < n and chk[nx][ny] == 0:
            if arr[nx][ny] < arr[x][y]:
                chk[nx][ny] = 1
                func(arr, nx, ny, chk, boom, cnt + 1, mval)
                chk[nx][ny] = 0
            elif boom == False:
                if arr[nx][ny] - k < arr[x][y]:
                    tmp = arr[nx][ny]
                    arr[nx][ny] = arr[x][y] - 1
                    chk[nx][ny] = 1
                    func(arr, nx, ny, chk, True, cnt + 1, mval)
                    arr[nx][ny] = tmp
                    chk[nx][ny] = 0
    mval[0] = max(mval[0], cnt)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, k = map(int, input().split(" "))
    arr = []
    mval = -1
    for i in range(n):
        arr.append(list(map(int, input().split(" "))))
        mval = max(max(arr[i]), mval)
    start = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == mval:
                start.append((i, j))
    mval = [-1]
    for x, y in start:
        chk = [[0] * n for _ in range(n)]
        chk[x][y] = 1
        func(arr, x, y, chk, False, 1, mval)
    print(f"#{test_case} {mval[0]}")
    # ///////////////////////////////////////////////////////////////////////////////////
