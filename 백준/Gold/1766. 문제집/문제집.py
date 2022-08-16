import collections, heapq
adj = collections.defaultdict(list)
indegree = [0 for _ in range(32001)]

N,M=map(int,input().split())
for _ in range(M):
    a,b=map(int,input().split())
    adj[a].append(b)
    indegree[b]+=1
queue = []
for i in range(1,N+1):
    if indegree[i]==0:
        heapq.heappush(queue,i)
        
while queue:
    u = heapq.heappop(queue)
    print(u,end=' ')
    for v in adj[u]:
        indegree[v]-=1
        if indegree[v]==0:
            heapq.heappush(queue,v)