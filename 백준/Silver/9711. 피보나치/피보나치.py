import collections
dp = collections.defaultdict(int)
dp[1]=1
dp[2]=1
for i in range(2,10101):
    dp[i]=dp[i-1]+dp[i-2]

for t in range(1,int(input())+1):
    p,q = map(int,input().split())
    print(f"Case #{t}:",dp[p]%q)