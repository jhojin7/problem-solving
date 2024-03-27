def solution(n):
    dp = [0,1,1,2,3,5]
    if n<=len(dp):
        return dp[n]%1234567
    for _ in range(n-len(dp)+1):
        dp.append(dp[-1]+dp[-2])
    return dp[n]%1234567
        