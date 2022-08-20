n,k = map(int,input().split())
dp = [0 for _ in range(k+1)]
arr = []
for _ in range(n):
    x = int(input())
    arr.append(x)
dp[0] = 1
for j in range(len(arr)):
    # print(dp)
    for i in range(k+1):
        if i+arr[j]>k: continue
        dp[i+arr[j]] += dp[i]
print(dp[k])