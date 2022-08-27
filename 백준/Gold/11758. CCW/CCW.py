import math
def angle(v1,v2):
    """if theta>0, ccw. if -, cw."""
    # v1,v2 = sorted((v1,v2))
    x1,y1=v1
    x2,y2=v2
    theta = (math.asin(
        (x1*y2-y1*x2)/
        (math.sqrt(x1*x1+y1*y1)
        *math.sqrt(x2*x2+y2*y2))
    ))
    return math.degrees(theta)
def vector(p1,p2):
    """make vector p1->p2"""
    ax,ay=p1
    bx,by=p2
    return (bx-ax,by-ay)

p1 = tuple(map(int,input().split()))
p2 = tuple(map(int,input().split()))
p3 = tuple(map(int,input().split()))
v12 = vector(p1,p2)
v23 = vector(p2,p3)
theta = angle(v12,v23)
if theta>0: print(1)
elif theta<0: print(-1)
else: print(0)