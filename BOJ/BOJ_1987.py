import sys


def func():
    dt = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    q = set()
    dic = 0
    dic |= 1 << arr[0][0]
    q.add((0, 0, dic, 1))
    global mval
    while q:
        x, y, dic, cnt = q.pop()
        mval = max(mval, cnt)
        for dx, dy in dt:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < r and 0 <= ny < c and dic & (1 << arr[nx][ny]) == 0:
                q.add((nx, ny, dic | (1 << arr[nx][ny]), cnt + 1))


r, c = map(int, sys.stdin.readline().split(" "))
arr = []
for _ in range(r):
    arr.append(list(map(lambda x: ord(x) - 65, list(sys.stdin.readline()))))
mval = 0
func()
print(mval)
