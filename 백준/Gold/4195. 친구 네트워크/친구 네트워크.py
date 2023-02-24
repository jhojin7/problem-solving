import collections
parent = collections.defaultdict(str)
rank = collections.defaultdict(int)

def find(u):
    cur = parent[u]
    while cur!=parent[cur]:
        parent[cur] = parent[parent[cur]]
        cur = parent[cur]
    return cur

def union(u,v):
    a,b = find(u),find(v)
    if a==b: return False
    if rank[a]>rank[b]:
        parent[b] = a
        rank[a]+=rank[b]
    else:
        parent[a] = b
        rank[b] += rank[a]
    return True

for t in range(int(input())):
    parent.clear()
    rank.clear()
    for f in range(int(input())):
        a,b = input().split()
        # init
        if a not in parent.keys(): parent[a] = a
        if b not in parent.keys(): parent[b] = b
        if a not in rank.keys(): rank[a] = 1
        if b not in rank.keys(): rank[b] = 1
        # union find
        union(a,b)
        print(rank[find(b)])