N,M = map(int, input().split())
xx = []
yy = []
for _ in range(M):
    x,y = map(int,input().split())
    xx.append(x)
    yy.append(y)

xavg = sorted(xx)[len(xx)//2]
yavg = sorted(yy)[len(yy)//2]

ans = 0
for x in xx:
    ans+=abs(xavg-x)
for y in yy:
    ans+=abs(yavg-y)

print(ans)