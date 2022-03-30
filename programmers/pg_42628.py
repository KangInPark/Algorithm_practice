from heapq import heappop, heappush


def solution(operations):
    h = []
    for item in operations:
        try:
            if item[0] == "I":
                tmp = int(item[2:])
                heappush(h, tmp)
            elif item == "D 1":
                h.remove(max(h))
            else:
                heappop(h)
        except:
            continue
    if not h:
        return [0, 0]
    else:
        answer = [max(h), heappop(h)]
        return answer
