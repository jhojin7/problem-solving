N=int(input())
arr=list(map(int,input().split()))
dp = [1 for _ in range(N)]
for i in range(N-1,-1,-1):
    for j in range(N-1,i,-1):
        if arr[j]<arr[i] and dp[j]+1>dp[i]:
            dp[i] = dp[j]+1
print(max(dp))