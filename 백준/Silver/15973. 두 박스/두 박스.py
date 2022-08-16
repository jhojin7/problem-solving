def intersect(a,b,c,d)->int:
    # a<=x<=b, c<=x<=d
    if a<=c<d<=b: 
        return d-c+1
    elif a<=c<b<=d:
        return b-c+1
    elif c<=a<d<=b:
        return d-a+1
    elif c<=a<b<=d:
        return b-a+1
    elif b<c:
        return 0
    elif d<a:
        return 0
    elif b==c:
        return 1
    elif d==a:
        return 1
    # abcd = 0101
    elif a==c and b==d:
        return b-a+1
    else: #????
        return 0

ax,ay,bx,by = map(int,input().split())
px,py,qx,qy = map(int,input().split())
xx = intersect(ax,bx,px,qx)
yy = intersect(ay,by,py,qy)

# dot
if xx==1 and yy==1: 
    print("POINT")
# line
elif (xx>1 and yy==1
    or xx==1 and yy>1): 
    print("LINE")
# rectangle
elif xx>1 and yy>1: 
    print("FACE")
# none
else: 
    print("NULL")