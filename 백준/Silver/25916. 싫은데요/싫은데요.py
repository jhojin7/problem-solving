N,M = map(int,input().split())
arr = list(map(int,input().split()))
ans = 0
s = 0
j =0
for i in range(N):
    while s<M and j<N:
        if s+arr[j]>M: break
        s+=arr[j]
        j+=1
    ans = max(ans,s)
    # print(i,j,s,ans)
    s-=arr[i]
print(ans)