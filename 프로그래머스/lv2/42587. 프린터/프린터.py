import collections

def solution(priorities, location):
    q = collections.deque([(p,i) for i,p in enumerate(priorities)])
    printcnt = 0
    loc = location
    while q:
        cur,idx = q.popleft()
        #print(cur,idx)
        ok=False
        for x,_ in q:
            if cur<x:
                q.append((cur,idx))
                ok=True
                break
        if ok: continue
        else: 
            printcnt+=1
            if idx==location:
                #print(idx,cur,printcnt)
                return printcnt
    