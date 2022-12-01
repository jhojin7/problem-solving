def solution(s):
    ans = 1
    x = s[0]
    a,b=1,0
    for i in range(1,len(s)):
        print(x,s[i],a,b,ans)
        if a==b:
            a,b=1,0
            ans+=1
            if i==len(s)-1:
                continue
            x = s[i]
        elif s[i]==x:
            a+=1
        elif s[i]!=x:
            b+=1
    return ans
            
        