while 1:
    try:
        x = list(map(int,input().split()))
        a,b = x.count(0),x.count(1)
        if a==1 and b==3: print("A")
        elif a==2 and b==2: print("B")
        elif a==3 and b==1: print("C")
        elif a==4 and b==0: print("D")
        elif a==0 and b==4: print("E")
    except:
        break