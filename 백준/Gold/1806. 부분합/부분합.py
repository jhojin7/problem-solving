N,S=map(int,input().split())
arr = list(map(int,input().split()))
pre = [0 for _ in range(N+1)]
s=0
for i in range(N):
    s+=arr[i]
    pre[i+1] = s

l,r = 0,1
ans=9999999
while l<=r and r<N+1:
    if pre[r]-pre[l]>=S:
        # print(arr[l:r])
        ans = min(ans,r-l)
        l+=1
    else:
        r+=1
if ans==9999999: print(0)
else: print(ans)