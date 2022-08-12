import math
i =0
while 1:
    i+=1
    try: r,w,l = map(int,input().split())
    except: break
    diag = math.sqrt(w*w+l*l)
    if diag<=r*2: print(f"Pizza {i} fits on the table.")
    else: print(f"Pizza {i} does not fit on the table.")