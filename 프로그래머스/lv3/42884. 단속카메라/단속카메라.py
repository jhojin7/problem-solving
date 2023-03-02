import math
def solution(routes):
    routes.sort()
    l,r = routes[0]
    cam=0
    for a,b in routes[1:]:
        #print(l,r)
        if r<a:
            cam+=1
            l,r = a,b
            #print(cam)
            continue
        l = max(l,a)
        r = min(r,b)
    #print(l,r,cam)
    return cam+1
        
        
    
    