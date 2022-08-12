import math
i = 0
while 1:
    i+=1
    a,b,c=map(int,input().split())
    if (a,b,c)==(0,0,0): break
    print(f"Triangle #{i}")
    try:
        if a==-1:
            ans = math.sqrt(c*c-b*b)
            if ans==0: raise ValueError
            print("a = {:.3f}".format(ans))
        elif b==-1:
            ans = math.sqrt(c*c-a*a)
            if ans==0: raise ValueError
            print("b = {:.3f}".format(ans))
        elif c==-1:
            ans = math.sqrt(a*a+b*b)
            if ans==0: raise ValueError
            print("c = {:.3f}".format(ans))
    except:
        print("Impossible.")
    print()