import sys, collections, heapq
V,E = map(int,sys.stdin.readline().split())
K = int(input())
graph = collections.defaultdict(list)
for _ in range(E):
    u,v,w = map(int,sys.stdin.readline().split())
    graph[u].append((v,w))
# print(graph)

dist = collections.defaultdict()
# priority queue with smallest weight on top
pqueue = [(0,K)] # weight, start
while pqueue:
    weight, node = heapq.heappop(pqueue)
    # update dist
    if node not in dist:
        dist[node] = weight
        # heappush adjacent node
        for v,w in graph[node]:
            heapq.heappush(pqueue,(weight+w,v))
    # print(pqueue, dist)

# print answer
for v in range(1,V+1):
    if v not in dist: print("INF")
    else: print(dist[v])