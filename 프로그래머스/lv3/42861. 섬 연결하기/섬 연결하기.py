import heapq, collections

parent = [i for i in range(111)]


def find(u):
    if parent[u]==u:
        return u
    parent[u] = find(parent[u])
    return parent[u]

def union(u,v):
    u,v = min(u,v),max(u,v)
    a,b = find(u),find(v)
    if a==b: return
    parent[b]=a

def solution(n, costs):
   #graph = collections.defaultdict(list)
   #for u,v,w in costs:
   #    graph[u].append((v,w))
   #    graph[v].append((u,w))
    edges = [(w,u,v) for u,v,w in costs]
    edges.sort()
    print(edges)
    mst = []
    for w,u,v in edges:
        if find(u)!=find(v):
            union(u,v)
            mst.append((u,v,w))
    print(mst)
    ans = 0
    for _,_,w in mst:
        ans+=w
    return ans
            
            
        
        