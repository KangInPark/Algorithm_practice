def convert(s):
    h, m = list(map(lambda x: int(x), s.split(":")))
    return h*60 + m

def rconvert(val):
    h = str(val//60)
    m = str(val % 60)
    if len(h) == 1:
        h = "0"+h
    if len(m) == 1:
        m = "0"+m
    return h + ":" + m

def solution(n, t, m, timetable):
    for idx in range(len(timetable)):
        timetable[idx] = convert(timetable[idx])
    timetable.sort()
    busStart = 540
    busmax = 540 + (n-1) * t
    mcnt = 0
    for i in range(len(timetable)):
        while busStart < timetable[i]:
            busStart += t
            mcnt = 0
            if(busmax < busStart):
                return rconvert(busmax)
        mcnt += 1
        if mcnt == m:
            busStart += t
            mcnt = 0
            if(busmax < busStart):
                return rconvert(timetable[i]-1)
    return rconvert(busStart)
