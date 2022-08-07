N=int(input())
A=list(map(int,input().split()))
dp1 = [1 for _ in range(N)]
dp2 = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if A[j]<A[i] and dp1[j]+1>dp1[i]:
            dp1[i] = dp1[j]+1
for i in range(N-1,-1,-1):
    for j in range(N-1,i,-1):
        if A[j]<A[i] and dp2[j]+1>dp2[i]:
            dp2[i] = dp2[j]+1
ans = [x+y-1 for x,y in zip(dp1,dp2)]
print(max(ans))