n = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(n + 1)]

for i in range(1, n):
    l = 0
    for j in range(i):
        if arr[j] < arr[i]:
            l = max(l, dp[j])
    dp[i] = l + 1
print(max(dp))