import math
def solution(routes):
    routes.sort(key=lambda x:x[1])
    cam = -30009
    ans = 0
    for a,b in routes:
        if cam<a:
            cam = b
            ans+=1
            continue
    return ans
