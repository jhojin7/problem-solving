N,K = map(int,input().split())
rooms = [[0,0] for _ in range(7)]
for _ in range(N):
    a,b = map(int,input().split())
    rooms[b][a] +=1
ans =0
for m,f in rooms:
    arr = [m%K,f%K]
    ans+=m//K
    ans+=f//K
    for aa in arr:
        if aa>0: ans+=1
print(ans)