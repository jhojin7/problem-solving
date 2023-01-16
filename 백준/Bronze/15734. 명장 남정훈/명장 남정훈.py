l,r,a = map(int,input().split())

while a:
    if l<r:
        a-=1
        l+=1
    elif l>r:
        a-=1
        r+=1
    elif a%2==0:
        l+=1
        r+=1
        a-=2
    else:
        l+=1
        a-=1
print(min(l,r)*2)