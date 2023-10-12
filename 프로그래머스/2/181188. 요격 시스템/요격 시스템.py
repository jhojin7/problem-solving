def solution(targets):
    x, ans = 0,0
    for s,e in sorted(targets):
        if s < x:
            x = min(e,x)
        else:
            x = e
            ans+=1
    return ans
            
            