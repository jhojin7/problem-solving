N=int(input())
T = [0 for _ in range(1500010)]
P = [0 for _ in range(1500010)]
for i in range(1,N+1):
    t,p = map(int,input().split())
    T[i]=t
    P[i]=p

dp=[0 for _ in range(N+10)]
prev=0 #?????????
for i in range(1,N+2):
    prev = max(prev, dp[i])
    if i+T[i]>N+1: continue
    dp[i+T[i]] = max(prev+P[i],dp[i+T[i]])
# print(dp)
print(max(dp))