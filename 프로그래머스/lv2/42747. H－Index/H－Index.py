import collections
def solution(cita):
    n = len(cita)
    cntr = collections.Counter(cita)
    h = 0
    for i,x in enumerate(sorted(cita,reverse=True),1):
        if x>=i:
            h = max(i,h)
    print(h)
    return h
