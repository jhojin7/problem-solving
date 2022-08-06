N=int(input())
M=int(input())
parent = [x for x in range(N+1)]
rank = [1 for _ in range(N+1)]

def find(u):
    cur = parent[u]
    while cur!=parent[cur]:
        parent[cur] = parent[parent[cur]]
        cur = parent[cur]
    return cur

def union(u,v):
    a,b = find(u),find(v)
    if a==b: return False
    if rank[a] > rank[b]:
        parent[b] = a
        rank[a] += rank[b]
    else:
        parent[a] = b
        rank[b] += rank[a]
    return True


for i in range(N):
    row = list(map(int,input().split()))
    for j,k in enumerate(row):
        if k==1: union(i+1,j+1)

travel = list(map(int,input().split()))
root = find(travel[0])
for t in travel:
    if find(t) != root:
        print("NO")
        exit()
print("YES")