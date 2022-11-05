N,M = map(int,input().split())
strs = []
for _ in range(N):
    strs.append(input().strip())
strs.sort()

def hamming(a,b):
    ans = 0
    for x,y in zip(a,b):
        if x!=y: ans+=1
    return ans

ans = ""
for j in range(M):
    a,c,g,t = 0,0,0,0
    for i in range(N):
        if strs[i][j]=='A': a+=1
        if strs[i][j]=='C': c+=1
        if strs[i][j]=='G': g+=1
        if strs[i][j]=='T': t+=1
    idx = [a,c,g,t].index(max([a,c,g,t]))
    ans+=("ACGT"[idx])
print(ans)
print(sum([hamming(ans,s) for s in strs]))