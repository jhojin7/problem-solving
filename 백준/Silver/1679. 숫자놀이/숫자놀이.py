N = int(input())
arr = sorted(list(map(int, input().split())))
K = int(input())
M = max(arr)*K
dp = [999999 for _ in range(M+2)]
dp[1] = 1

for i in range(1, M+2):
    if i in arr:
        dp[i] = 1
    else:
        for j in range(1, i//2+1):
            dp[i] = min(dp[i], dp[j]+dp[i-j])
    if dp[i] > K:
        print(f'{"holsoon" if i%2==0 else "jjaksoon"} win at {i}')
        break
