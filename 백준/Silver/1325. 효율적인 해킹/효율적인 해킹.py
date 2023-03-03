import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()

N,M = map(int,input().split())

graph = collections.defaultdict(list)
for _ in range(M):
    u,v = map(int,input().split())
    graph[v].append(u)

def find(u):
    q = collections.deque([u])
    vis = [False for _ in range(N+1)]
    cnt=0
    while q:
        cur = q.popleft()
        # if cur in vis: continue
        # vis.add(cur)
        if vis[cur]: continue
        vis[cur] = True
        cnt+=1
        for nxt in graph[cur]:
            q.append(nxt)
    # return len([x for x in vis if x])
    return cnt

ans = collections.defaultdict(list)
for u in range(1,N+1):
    ans[find(u)].append(u)
print(*sorted(ans[max(ans.keys())]))
