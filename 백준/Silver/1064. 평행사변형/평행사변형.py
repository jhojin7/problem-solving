import math
ax,ay,bx,by,cx,cy = map(int,input().split())
if (ax==bx==cx
    or ay==by==cy
    or (by-ay)*(cx-bx)==(cy-by)*(bx-ax)
    ): print(-1)
else:
    d1 = math.sqrt((bx-ax)**2+(by-ay)**2)
    d2 = math.sqrt((cx-bx)**2+(cy-by)**2)
    d3 = math.sqrt((cx-ax)**2+(cy-ay)**2)
    maxperi = max(2*(d1+d2),2*(d2+d3),2*(d3+d1))
    minperi = min(2*(d1+d2),2*(d2+d3),2*(d3+d1))
    print(maxperi-minperi)