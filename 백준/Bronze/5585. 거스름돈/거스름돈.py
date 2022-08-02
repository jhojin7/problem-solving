n=1000-int(input())
ans = 0
while n>0:
    if n>=500: 
        n-=500
        ans+=1
    elif n>=100: 
        n-=100
        ans+=1
    elif n>=50: 
        n-=50
        ans+=1
    elif n>=10: 
        n-=10
        ans+=1
    elif n>=5: 
        n-=5
        ans+=1
    else:
        n-=1
        ans+=1

print(ans)