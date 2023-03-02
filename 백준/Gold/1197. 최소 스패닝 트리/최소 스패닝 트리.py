import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()

V,E = inputint()
# graph = collections.defaultdict(list)
edges = []
for _ in range(E):
    u,v,w = inputint()
    edges.append((w,u,v))
edges.sort()

parent=[i for i in range(V+1)]
def find(u):
    if u==parent[u]:
        return u
    parent[u]=find(parent[u])
    return parent[u]
def union(u,v):
    u,v = min(u,v),max(u,v)
    u,v = find(u),find(v)
    if u==v: return
    parent[v] = u

mst = []
for w,u,v in edges:
    if find(u)!=find(v):
        union(u,v)
        mst.append((u,v,w))
ans =0
for _,_,w in mst:
    ans+=w
print(ans)