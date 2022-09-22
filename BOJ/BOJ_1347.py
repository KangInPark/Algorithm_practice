import sys

arr = [["#"] * 101 for i in range(101)]
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
v = 0
x = 50
y = 50

arr[x][y] = "."
for cmd in s:
    if cmd == "R":
        v = (v + 1) % 4
    elif cmd == "L":
        v = (v + 3) % 4
    else:
        x += d[v][0]
        y += d[v][1]
        arr[x][y] = "."
minx = 102
miny = 102
maxx = -1
maxy = -1
for i in range(101):
    for j in range(101):
        if arr[i][j] == ".":
            minx = min(i, minx)
            maxx = max(i, maxx)
            miny = min(j, miny)
            maxy = max(j, maxy)
for i in range(minx, maxx + 1):
    for j in range(miny, maxy + 1):
        print(arr[i][j], end="")
    print("")
