import math
while 1:
    x,y = map(int,input().split())
    if (x,y)==(0,0): break
    try: 
        rad = math.atan2(y,x)
        ans = rad*180/math.pi
    except: ans = 0
    print(round(ans))