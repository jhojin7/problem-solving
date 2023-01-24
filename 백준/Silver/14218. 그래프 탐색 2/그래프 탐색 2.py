import sys,collections, heapq,math
input=sys.stdin.readline

n,m = map(int,input().split())
graph = collections.defaultdict(list)
for _ in range(m):
    v,w = map(int,input().split())
    graph[v].append(w)
    graph[w].append(v)
q = int(input())
dist = [math.inf for _ in range(n+1)]
for _ in range(q):
    v,w = map(int,input().split())
    graph[v].append(w)
    graph[w].append(v)

    dist[1]=0
    queue = []
    heapq.heappush(queue,(0,1))
    vis=set()
    while queue:
        cnt,cur = heapq.heappop(queue)
        if cur in vis: continue
        vis.add(cur)
        if dist[cur]<cnt: continue
        for nxt in graph[cur]:
            if cnt < dist[nxt]:
                dist[nxt] = cnt+1
                heapq.heappush(queue,(cnt+1,nxt))
    for d in dist[1:]:
        if d==math.inf: print(-1,end=' ')
        else: print(d,end=' ')
    print()