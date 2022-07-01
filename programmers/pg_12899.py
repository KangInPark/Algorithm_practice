def solution(n):
    answer = ""
    n -= 1
    tmp = ["1", "2", "4"]
    while n >= 0:
        answer += tmp[n % 3]
        n = n // 3 - 1
    answer = answer[::-1]
    return answer
