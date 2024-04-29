def solution(t, p):
    l = len(p)
    ans =0 
    for i in range(len(t)-len(p)+1):
        aa,bb = (int(p), int(t[i:i+l]))
        if aa>=bb: ans+=1
    return ans
        