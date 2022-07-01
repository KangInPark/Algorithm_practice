import sys


def solution(record):
    dic = {}
    answer = []
    for s in record:
        cmd = s.split(" ")
        if cmd[0] == "Enter":
            dic[cmd[1]] = cmd[2]
        elif cmd[0] == "Change":
            dic[cmd[1]] = cmd[2]
    for s in record:
        cmd = s.split(" ")
        if cmd[0] == "Enter":
            answer.append(dic[cmd[1]] + "님이 들어왔습니다.")
        elif cmd[0] == "Leave":
            answer.append(dic[cmd[1]] + "님이 나갔습니다.")
    return answer
