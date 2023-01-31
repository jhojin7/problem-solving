N=300
dp = [0 for _ in range(N)]
dp[:4]=[1,1,3,5] #https://www.acmicpc.net/board/view/69111
for i in range(4,N):
    # dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    dp[i] = dp[i-1]+2*dp[i-2]
while 1:
    try: n=int(input())
    except: break
    print(dp[n])