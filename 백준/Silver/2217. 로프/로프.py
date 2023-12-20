N=int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort(reverse=True)
ans = 0
for k,w in enumerate(arr,1):
    ans=max(ans,w*k)
print(ans)