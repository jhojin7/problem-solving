import sys
input = sys.stdin.readline

x,y = map(int,input().split())

z = (y*100)//x
if z>=99:
    print(-1)
    exit()

l,r = 1,x
ans = 0
while l<=r:
    m = (l+r)//2
    zz = (y+m)*100//(x+m)
    if zz<=z:
        l = m+1
    else:
        ans = m
        r = m-1
print(ans)