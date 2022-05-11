"""
https://leetcode.com/submissions/detail/697483631/
"""
from __solver import *

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        # init graph
        for u,v,w in times:
            # print(u,v,w)
            graph[u].append((v,w))
        # print(graph)
        # init dict for distance
        dist = collections.defaultdict()
        # pqueue (travel time, to node)
        Q = [(0,k)]
        # dijkstra
        while Q:
            time, node = heapq.heappop(Q)
            # if node not visited, visit
            if node not in dist:
                dist[node] = time
                # breadth edes and nodes
                for v,w in graph[node]:
                    # heappush (current time, node)
                    heapq.heappush(Q,(time+w,v))
        # if all node visited, 
        if len(dist) == n:
            # return time it took to visit all.
            return max(dist.values()) 
        # else, return -1
        return -1

inputs = [
[[2,1,1],[2,3,1],[3,4,1]],4,2
,[[1,2,1]],2,1
,[[1,2,1]],2,2
]
while inputs:
    Solver.solve(Solution,inputs.pop(0),inputs.pop(0),inputs.pop(0))