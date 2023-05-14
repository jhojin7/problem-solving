import sys; input = sys.stdin.readline
N=int(input())
arr = list(map(int,input().split()))
ans =0
for i in range(N):
    j = i+1
    while j<N and arr[j-1]<arr[j]:
        ans = max(ans,arr[j]-arr[i])
        j = j+1
print(ans)