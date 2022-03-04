import sys

n = int(sys.stdin.readline())
chk = 0
ret = ""
for i in range(n):
    cmd = sys.stdin.readline().rstrip().split(" ")
    if cmd[0] == "add":
        chk |= (1<<int(cmd[1]))
    elif cmd[0] == "remove":
        chk &= ~(1<<int(cmd[1]))
    elif cmd[0] == "check":
        if chk & (1<<int(cmd[1])):
            print(1)
        else:
            print(0)
    elif cmd[0] == "toggle":
        chk ^= (1<<int(cmd[1]))
    elif cmd[0] == "all":
        chk = (1<<21)-1
    else:
        chk = 0