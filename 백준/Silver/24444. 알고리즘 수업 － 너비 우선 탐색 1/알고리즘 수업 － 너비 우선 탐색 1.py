import sys, collections, heapq, math, re, random
input=sys.stdin.readline

N,M,K = map(int,input().split())
graph = collections.defaultdict(list)
for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(M):
    graph[i].sort()

vis = set()
ans = [0 for _ in range(N+1)]
q = collections.deque([K])
cnt=1
while q:
    cur = q.popleft()
    if cur in vis: continue
    vis.add(cur)
    ans[cur]=cnt
    cnt+=1
    for nxt in graph[cur]:
        q.append(nxt)
# print(vis)
# for i in range(1,N+1):
#     try: ans[i] = vis.index(i)+1
#     except: pass
print(*ans[1:],sep='\n')