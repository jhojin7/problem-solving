import sys,collections,heapq,math
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = collections.defaultdict(list)
for _ in range(M):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
src,dest = map(int,input().split())
# print(graph)
# print(src,dest)

dist = [math.inf for _ in range(N+1)]
prev = [0 for _ in range(N+1)]
# 시작을 dist[src]로
dist[src] = 0
pq =[(dist[src],src)] 
while pq:
    w,u = heapq.heappop(pq)
    # print(u,w)
    if dist[u] != w: continue #???
    for vv,ww in graph[u]:
        if dist[vv] <= dist[u]+ww: continue
        dist[vv] = dist[u]+ww
        heapq.heappush(pq,(dist[vv],vv))
        prev[vv] = u

# build route
route = []
cur = dest
while cur != src:
    route.append(cur)
    cur = prev[cur]
route.append(cur)
route.reverse()#!!!!!!!!!!!

# prints
print(dist[dest])
print(len(route))
print(*route)