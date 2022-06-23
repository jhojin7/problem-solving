""" Shorts """

""" 2407 조합"""
def factorial(x):
    if x == 1 or x == 0: return 1
    elif x == 2: return 2
    return factorial(x-1) * x
# n,m = map(int, input().split())
n,m = 100, 6
dp = [1,1,2] 
for i in range(3,100+1):
    dp.append(dp[i-1]*i)
    # dp[i] = dp[i-1] * i
print((dp[n]//dp[n-m])//dp[m])