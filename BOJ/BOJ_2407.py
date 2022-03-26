n, m = map(int, input().split(" "))
arr = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if j > i:
            break
        elif j == 1:
            arr[i][j] = i
        elif i == j:
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
print(arr[n][m])
