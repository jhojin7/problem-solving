import math
points = []
for i in range(int(input())):
    x,y,v = map(int,input().split())
    points.append((x,y,v,i))
T = []
for x,y,v,i in points:
    t = math.sqrt(x*x+y*y)/v
    T.append((t,i))
T.sort()
for _,i in T:
    print(i+1)