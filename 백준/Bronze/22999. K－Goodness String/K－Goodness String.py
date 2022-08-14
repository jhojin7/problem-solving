for t in range(int(input())):
    n,k = map(int,input().split())
    s = input().strip()
    cur = 0 
    l,r = 0,len(s)-1
    while l<r:
        # print(s[l],s[r])
        if s[l]!=s[r]: cur+=1
        l+=1; r-=1
    print(f"Case #{t+1}: {abs(k-cur)}")