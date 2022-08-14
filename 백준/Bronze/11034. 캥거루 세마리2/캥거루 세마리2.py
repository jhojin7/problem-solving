while 1:
    try: 
        a,b,c=map(int,input().split())
        d = b-a-1
        e = c-b-1
        if d==0: print(e)
        elif e==0: print(d)
        elif d>e: print(d)
        elif d<e: print(e)
        else: print(d)
    except: break