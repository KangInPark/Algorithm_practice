A = input()
B = input()

arr = [[0] * (len(A) + 1) for _ in range(len(B) + 1)]
for i in range(1, len(B) + 1):
    for j in range(1, len(A) + 1):
        if B[i - 1] == A[j - 1]:
            arr[i][j] = arr[i - 1][j - 1] + 1
        else:
            arr[i][j] = max(arr[i][j - 1], arr[i - 1][j])
print(arr[len(B)][len(A)])
