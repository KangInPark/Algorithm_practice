import sys


def func():
    mval = sys.maxsize
    ret = [-1, -1, -1]
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            tmp = arr[i] + arr[left] + arr[right]
            if tmp < 0:
                if -tmp < mval:
                    mval = -tmp
                    ret = [arr[i], arr[left], arr[right]]
                left += 1
            elif tmp > 0:
                if tmp < mval:
                    mval = tmp
                    ret = [arr[i], arr[left], arr[right]]
                right -= 1
            else:
                ret = [arr[i], arr[left], arr[right]]
                return ret
    return ret


n = int(input())
arr = list(map(int, input().split(" ")))
arr.sort()
ret = func()
print(" ".join(map(str, ret)))
