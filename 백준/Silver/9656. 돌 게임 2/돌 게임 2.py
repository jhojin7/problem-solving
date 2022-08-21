n=int(input())
dp = [-1 for _ in range(1001)]
sk = 1; cy = 2
dp[1] = sk
for i in range(1,n+1):
    if i+3>1000: break
    if dp[i]==sk: dp[i+1]=cy
    else: dp[i+1]=sk
    if dp[i]==sk: dp[i+3]=cy
    else: dp[i+3]=sk#########
if dp[n]==cy:print("SK")
else: print("CY")