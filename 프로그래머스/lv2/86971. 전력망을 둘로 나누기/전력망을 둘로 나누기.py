import collections
def solution(n, wires):
    graph = collections.defaultdict(list)
    for u,v in wires:
        graph[u].append(v)
        graph[v].append(u)
    print(graph)
    def bfs(src,cutedge):
        q = collections.deque([src])
        vis = set()
        while q:
            cur = q.popleft()
            if cur in vis: continue
            vis.add(cur)
            for nxt in graph[cur]:
                if (cur,nxt)==cutedge or (nxt,cur)==cutedge:
                    continue
                q.append(nxt)
        return vis
    #print(bfs(4,wires[5]),bfs(7,wires[5]))
    ans = 999999
    for u,v in wires:
        A,B = (bfs(u,(u,v)),bfs(v,(u,v)))
        diff = abs(len(A)-len(B))
        ans = min(ans,diff)
    print(ans)
    return ans