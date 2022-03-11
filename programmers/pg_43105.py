def solution(triangle):
    answer = 0
    arr = [[0] * len(triangle) for _ in range(len(triangle))]
    arr[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j-1 >= 0:
                arr[i][j] = max(arr[i-1][j], arr[i-1][j-1]) + triangle[i][j]
            else:
                arr[i][j] = arr[i-1][j] + triangle[i][j]
    return max(arr[-1])