N=int(input())
arr=[]
sx,sy,ex,ey = map(int,input().split())
for i in range(N):
    M=int(input())
    a,b=map(int,input().split())
    dist=abs(sx-a)+abs(sy-b)
    for _ in range(M-1):
        c,d=map(int,input().split())
        dist+=abs(a-c)+abs(b-d)
        a,b=c,d
    dist+=abs(a-ex)+abs(b-ey)
    arr.append(dist)
print(arr.index(min(arr))+1)