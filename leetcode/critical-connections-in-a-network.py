"""
somewhat correct. different approach needed.
https://leetcode.com/submissions/detail/701944961/
"""
from __solver import *
class Solution:
    def dfs(edges, connections, edge, visited):
        visited.append(edge)
        pass
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # prep edges
        edges = collections.defaultdict(list)
        sorted_connections = []
        for a,b in connections:
            # double check to make sure a<b
            a,b = min(a,b),max(a,b)
            # fill in dict
            edges[a].append((a,b))
            edges[b].append((b,a))
            sorted_connections.append((a,b))
            # if b not in edges dict, make empty list
            if b not in edges.keys():
                edges[b] = []
        # sort connections
        connections = sorted(sorted_connections)
        print(n,edges,connections)
        # # return key with a single edge
        # for arr in edges.values():
        #     if len(arr)==1: 
        #         print(arr)
        #         return arr 

        # check every edge to see if other connections from a-b exists in graph
        for src,dest in connections: 
            print("src dest",src,dest)
            # dfs
            visited = []
            # dfs(edges, connections, , visited)


            # # bfs
            # queue = collections.deque(edges[src])
            # # visited = [(src,dest),(dest,src)]
            # while queue:
            #     if len(queue)>10:return
            #     print("queue",queue)
            #     x,y = queue.popleft()
            #     # if (x,y) in visited: continue
            #     # visited.append((x,y))
            #     # visited.append((y,x))
            #     print("xy",x,y)
            #     # if dest==y, there IS an alternate route for (src,dest)
            #     if dest == y: 
            #         print(">> alternate route exist")
            #         break
            #     # traverse edges in range
            #     for edge in edges[y]:
            #         print(edge, (a,b))
            #         # dont append a,b
            #         if edge != (a,b): queue.append(edge)
        pass
# 4
# [[0,1],[1,2],[2,0],[1,3]]
# 2
# [[0,1]]
# Solution.criticalConnections(Solution,4,[[0,1],[1,2],[2,0],[1,3]])
Solution.criticalConnections(
    Solution,6,[[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]])