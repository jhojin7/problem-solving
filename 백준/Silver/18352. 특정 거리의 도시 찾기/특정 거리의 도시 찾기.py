import collections, heapq

N,M,K,X = map(int,input().split())
graph = collections.defaultdict(list)
for i in range(M):
    A,B = map(int,input().split())
    graph[A].append(B)
# print(graph)

dist = collections.defaultdict(int)
pq = [(0,X)]
while pq:
    t,u = heapq.heappop(pq)
    if u in dist:
        continue
    dist[u] = t
    for v in graph[u]:
        heapq.heappush(pq,((t+1),v))
# print(sorted(dist.items()))
ok=False
for k,v in (sorted(dist.items())):
    if v==K:
        print(k)
        ok=True
if not ok: print(-1)