for _ in range(int(input())):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    if x1==x2 and y1==y2:
        # if 0 0 0 0 0 0 
        if x1==0 and y1==0 and r1==0: print(1)
        elif r1==0 and r2==0: print(1) 
        elif r1==r2: print(-1)
        else: print(0)
        #???
    else:
        d_sq = ((x1-x2)**2+(y1-y2)**2)
        if r1<r2: r1,r2 = r2,r1
        if (r1+r2)**2==d_sq: print(1)
        elif (r1-r2)**2==d_sq: print(1)
        elif (r1+r2)**2<d_sq: print(0)
        elif (r1-r2)**2>d_sq: print(0)
        elif (r1+r2)**2>d_sq: print(2)
        elif (r1-r2)**2<d_sq: print(2)