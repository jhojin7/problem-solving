import sys; input = sys.stdin.readline
N,M = map(int,input().split())
arr = list(map(int,input().split()))
ans = 0

if arr[0]==M: ans+=1
for i in range(1,N):
    arr[i] += arr[i-1]
    if arr[i]==M: ans+=1

for i in range(1,N):
    if arr[i]<M: continue
    for j in range(i,-1,-1):
        # print(i,j,arr[i],arr[j])
        if arr[i]-arr[j]==M:
            ans+=1
print(ans)