import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()

N=int(input())
M=int(input())
edges = []
for _ in range(M):
    u,v,w = map(int,input().split())
    edges.append((w,u,v))
edges.sort()

parent = [u for u in range(N+1)]
def find(u):
    if u==parent[u]:
        return parent[u]
    parent[u] = find(parent[u])
    return parent[u]
def union(u,v):
    u,v = min(u,v),max(u,v)
    u,v = find(u),find(v)
    if u==v: return 
    parent[v]=u

mst = []
for w,u,v in edges:
    if find(u)!=find(v):
        union(u,v)
        mst.append(w)

print(sum(mst))