import collections, heapq, math

N,M,R = map(int,input().split())
items = [0]+list(map(int,input().split()))
graph = collections.defaultdict(list)
for _ in range(R):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

def dijk(x):
    ret = 0
    vis = set()
    dist = [math.inf for _ in range(N+1)]
    dist[x]=0
    pq = [(0,x)]

    while pq:
        w,u = heapq.heappop(pq)
        # print(u)
        # if w>=M: break
        # if u in vis: continue
        # vis.add(u)
        
        # ret+=items[u]
        for v,ww in graph[u]:
            dist[u] = w
            if ww+w>M: continue
            heapq.heappush(pq,(ww+w,v))
    # print(dist)
    ret = sum([items[i] for i in range(1,N+1) if dist[i]<=M])
    return ret

ans = 0
for x in range(1,N+1):
    di = dijk(x)
    ans = max(ans,di)
    # print(di)
print(ans)