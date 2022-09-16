a,b,c=list(map(int,input().split()))
cnt=0
while 1:
    if b-a>c-b:
        if b-a>=2:
            c=a+1
        elif c-b>=2:
            a=b+1
        else:
            break
    else:
        if c-b>=2:
            a=b+1
        elif b-a>=2:
            c=a+1
        else:
            break
    a,b,c=sorted([a,b,c])
    cnt+=1
# print(a,b,c,cnt)
print(cnt)