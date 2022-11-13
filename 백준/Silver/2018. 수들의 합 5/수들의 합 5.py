import sys
input=sys.stdin.readline
N = int(input())

ans=0
l,r,s = 1,1,1
while l<=r:
    if s==N:
        ans+=1
    if s<N:
        r+=1
        s+=r
    else:
        s-=l
        l+=1
print(ans)