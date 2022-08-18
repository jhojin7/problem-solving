import sys,collections
input = sys.stdin.readline

def bfs(src):
    visited = set()
    edgescnt = 0
    queue = collections.deque([src])
    while queue:
        u = queue.popleft()
        # is cycle
        if u in visited: break
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                edgescnt+=1
                queue.append(v)
    # return len(visited)
    return (visited, edgescnt)

case_i = 1
while True:
    graph = collections.defaultdict(set)
    n,m = map(int,input().split())
    if n==0 and m==0: break
    for _ in range(m):
        u,v = map(int,input().split())
        graph[u].add(v)
        graph[v].add(u)
    # print(graph)

    # check for trees
    returns = []
    treecnt = 0
    for u in range(1,n+1):
        ret = bfs(u)
        if ret not in returns:
            returns.append(ret)
    # print(returns)
    for nodes,edgescnt in returns:
        if len(nodes)-1==edgescnt: treecnt+=1
    # print(treecnt)

    if treecnt==0:
        print(f"Case {case_i}: No trees.")
    elif treecnt==1:
        print(f"Case {case_i}: There is one tree.")
    else:
        print(f"Case {case_i}: A forest of {treecnt} trees.")
    case_i += 1