import collections, heapq
N,M,X = map(int,input().split())
graph = collections.defaultdict(list)
for i in range(M):
    u,v,t = map(int,input().split())
    graph[u].append((v,t))

def dijkstra(src,dest):
    dist = collections.defaultdict(int)
    pq = [(0,src)]
    while pq:
        t,u = heapq.heappop(pq)
        if u in dist:
            continue
        dist[u] = t
        for v,time in graph[u]:
            heapq.heappush(pq,((t+time),v))
    return dist[dest]

ans = 0
for v in range(1,N+1):
    # print(dijkstra(X,v),dijkstra(v,X))
    ans = max(ans,dijkstra(X,v)+dijkstra(v,X))
print(ans)