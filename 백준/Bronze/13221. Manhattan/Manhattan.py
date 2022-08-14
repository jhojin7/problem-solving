x,y = map(int,input().split())
xx,yy=0,0
mindist = 9999999
for _ in range(int(input())):
    a,b = map(int,input().split())
    taxidist = abs(x-a)+abs(y-b)
    if taxidist < mindist:
        xx,yy = a,b
        mindist = taxidist
print(xx,yy)