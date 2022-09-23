# import collections
T,P=[],[]
N=int(input())
for _ in range(N):
    t,p=map(int,input().split())
    T.append(t)
    P.append(p)
# print(T,P)

dp = [0 for _ in range(N+1)]
for i in range(N-1,-1,-1):
    tmp = i+T[i]
    if tmp>N: dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1],dp[tmp]+P[i])
print(dp[0])