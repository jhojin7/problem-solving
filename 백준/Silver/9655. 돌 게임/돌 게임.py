N=int(input())
dp = ['' for _ in range(1001)]
dp[1] = "SK"
for i in range(1,N+1):
    if i+3>1000: break
    if dp[i]=="CY":
        dp[i+1]="SK"
    else:
        dp[i+1]="CY"
    if dp[i]=="CY":
        dp[i+3]="SK"
    else:
        dp[i+3]="CY"
print(dp[N])
# print(dp)