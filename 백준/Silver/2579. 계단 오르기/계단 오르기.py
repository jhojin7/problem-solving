N=int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
dp = [0 for _ in range(N)]

if len(arr)==1:
    print(arr[0])
else:
    dp[0] = arr[0]
    dp[1] = arr[0]+arr[1]
    for i in range(2,N):
        dp[i] = max(
            arr[i]+arr[i-1]+dp[i-3],#....
            arr[i]+dp[i-2],
        )
    print(dp[-1])