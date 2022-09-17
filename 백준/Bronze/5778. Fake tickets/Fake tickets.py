import collections
while 1:
    N,M=map(int,input().split())
    if (N,M)==(0,0): break
    arr=list(map(int,input().split()))
    cnter=collections.Counter(arr)
    ans=0
    for k,v in cnter.items():
        if v>1: ans+=1
    print(ans)