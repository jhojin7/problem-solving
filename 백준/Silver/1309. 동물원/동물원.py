N=int(input())
dp =[0 for _ in range(N+5)]
dp[0] = 1
dp[1] = 1+2
dp[2] = 1+4+2
dp[3] = 1+6+8+2
dp[4] = 1+8+20+10+2

for i in range(5,N+1):
    # # dp[i] = dp[i-2]*2+dp[i-1]
    # dp[i] = 2*(dp[i-1]+dp[i-2]+dp[i-3])+1
    dp[i] = (dp[i-2]+dp[i-1]*2)%9901 
    #;;;;
print(dp[N]%9901)