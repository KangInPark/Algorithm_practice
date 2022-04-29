T = int(input())
r = 10**9 + 7
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, k = map(int, input().split(" "))
    arr = list(map(int, input().split(" ")))
    asum = 0
    bsum = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                continue
            if arr[i] > arr[j]:
                asum += 1
                if i < j:
                    bsum += 1
    ret = (bsum * k) % r
    ret += (asum * k * (k - 1) // 2) % r
    print(f"#{test_case} {ret%r}")
    # ///////////////////////////////////////////////////////////////////////////////////
