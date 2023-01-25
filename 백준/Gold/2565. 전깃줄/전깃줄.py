# lis...
N=int(input())
arr = [tuple(map(int,input().split())) for _ in range(N)]
arr.sort()
B = [b for a,b in arr]
cnt=1
maxcnt=1

dp = [1 for _ in range(N)]
for i in range(N):
    dp[i]= 1
    for j in range(i):
        if B[i]>B[j]:
            dp[i] = max(dp[i],dp[j]+1)

# print(B)
# print(dp)
print(N-max(dp))