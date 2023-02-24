N,M = map(int,input().split())
N = N+1
parent = [x for x in range(N)]
rank = [1 for _ in range(N)]

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

for _ in range(M):
    q,a,b = map(int,input().split())
    if q==0: union(a,b)
    elif q==1: 
        if find(a)==find(b): print("yes")
        else: print("no")
        # if parent[a] == parent[b]: print("yes")
        # else: print("no")
