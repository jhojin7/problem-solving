N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)
ans=0
for i in range(N):
    tip = arr[i]-i
    if tip>0: ans+=tip
print(ans)