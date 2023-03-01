import collections

def solution(progresses, speeds):
    arr = [(a,b) for a,b in zip(progresses,speeds)]
    d = [0 for _ in range(101)]
    ans = []
    cur = 0
    for a,b in arr:
        r = (100-a)%b
        if r!=0: r=1
        x = (100-a)//b+r
        cur = max(cur,x)
        d[cur]+=1
    d = [x for x in d if x!=0]
    return d