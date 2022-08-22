arr=list(input().strip())
brr=sorted(arr,reverse=True)
b=int(''.join(brr))
if b%30==0:
    print(b)
else:print(-1)