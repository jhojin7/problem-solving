N = int(input())
ans = []
for i in range(2,N+1):
    while N%i==0:
        if N%i == 0:
            ans.append(i)
            N/=i
print(*ans,sep='\n')