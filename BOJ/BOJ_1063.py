import sys

arr = [[0] * 8 for i in range(8)]
d = {
    "R": (0, 1),
    "L": (0, -1),
    "B": (1, 0),
    "T": (-1, 0),
    "RT": (-1, 1),
    "LT": (-1, -1),
    "RB": (1, 1),
    "LB": (1, -1),
}
s = sys.stdin.readline().strip().split(" ")
x = 8 - int(s[0][1])
y = ord(s[0][0]) - 65
arr[8 - int(s[1][1])][ord(s[1][0]) - 65] = 1
for i in range(int(s[2])):
    cmd = sys.stdin.readline().strip()
    nx = x + d[cmd][0]
    ny = y + d[cmd][1]
    if nx < 8 and ny < 8 and nx >= 0 and ny >= 0:
        if arr[nx][ny] == 1:
            tmpx = nx + d[cmd][0]
            tmpy = ny + d[cmd][1]
            if tmpx < 8 and tmpy < 8 and tmpx >= 0 and tmpy >= 0:
                arr[nx][ny] = 0
                arr[tmpx][tmpy] = 1
                x = nx
                y = ny
        else:
            x = nx
            y = ny
print(chr(y + 65) + str(8 - x))
for i in range(8):
    for j in range(8):
        if arr[i][j] == 1:
            print(chr(j + 65) + str(8 - i))
            break
