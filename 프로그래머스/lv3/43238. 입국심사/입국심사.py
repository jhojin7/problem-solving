def solution(n, times):
    l,r = 1,max(times)*n
    ans = 0
    while l<=r:
        m = (l+r)//2
        x = 0
        for t in times:
            x+=m//t
            if x>=n: break
        if n>x:
            l=m+1
        else: 
            ans = m
            r=m-1
    return ans
