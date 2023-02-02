N,M = map(int,input().split())
lanes = []
for _ in range(N):
    lanes.append(list(input().strip()))
ans = [-1 for _ in range(N+1)]
cnt=1
for j in range(M-1,-1,-1):
    col = [lanes[i][j] for i in range(N)]
    nums = [int(n) for n in col if n in "123456789"]
    ok=False
    for n in nums:
        if ans[n]==-1:
            ans[n]=cnt
            ok=True
    if ok: cnt+=1
print(*[n for n in ans if n!=-1],sep='\n')