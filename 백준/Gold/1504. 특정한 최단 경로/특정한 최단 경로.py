import sys,collections,heapq

def dijkstra(src,dest):
    pqueue = [(0,src)] # cost,start
    dist = collections.defaultdict()
    while pqueue:
        cost,node = heapq.heappop(pqueue)
        if node in dist: continue
        dist[node] = cost
        # if dest, break after updating dist
        if node == dest: break 
        for _cost,v in graph[node]:
            heapq.heappush(pqueue,(cost+_cost,v))
    if dest not in dist:
        return -1
    return dist[dest]

input = sys.stdin.readline
N,M = map(int,input().split())
graph = collections.defaultdict(list)
for _ in range(M):
    u,v,cost = map(int,input().split())
    graph[u].append((cost,v))
    graph[v].append((cost,u))

v1,v2 = map(int,input().split())

path1, path2 = 0,0
# 1-v1-v2-N
paths1 = [dijkstra(1,v1),dijkstra(v1,v2),dijkstra(v2,N)]
if -1 in paths1: path1 = -1
else: path1 = sum(paths1)
# 1-v2-v1-N
paths2 = [dijkstra(1,v2),dijkstra(v2,v1),dijkstra(v1,N)]
if -1 in paths2: path2 = -1
else: path2 = sum(paths2)

if path1==-1 and path2==-1:
    print(-1)
elif path1==-1:
    print(path2)
elif path2==-1:
    print(path1)
else:
    print(min(path1, path2))