N=int(input())
A = list(map(int,input().split()))
dp  = [1 for _ in range(N+1)]
incrsum  = [A[i] for i in range(N)]
for i in range(N):
    for j in range(i,-1,-1):
        if A[i]>A[j]:# and dp[j+1]!=dp[j]: 
            incrsum[i] = max(incrsum[j]+A[i],incrsum[i])
    # print(incrsum)
print(max(incrsum))
# print(dp)