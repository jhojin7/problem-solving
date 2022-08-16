for _ in range(4):
    ax,ay,bx,by,px,py,qx,qy = map(int,input().split())
    Ax = set(range(ax,bx+1))
    Ay = set(range(ay,by+1))
    Bx = set(range(px,qx+1))
    By = set(range(py,qy+1))
    xx = (Ax.intersection(Bx))
    yy = (Ay.intersection(By))
    # print(len(xx),len(yy))
    # dot
    if len(xx)==1 and len(yy)==1: 
        print('c')
    # line
    elif (len(xx)>1 and len(yy)==1
        or len(xx)==1 and len(yy)>=1): 
        print('b')
    # rectangle
    elif len(xx)>=1 and len(yy)>=1: print('a')
    # none
    else: print('d')