"""
time limit
https://leetcode.com/submissions/detail/699233570/
"""
from __solver import *

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # delay list for storing edge weight
        delay = []
        # deque
        edges = collections.defaultdict(list)
        # init deque, edges dict
        for u,v,w in times:
            edges[u].append((u,v,w))
        # bfs
        # k = starting point
        # deque = collections.deque(edges[k]) 
        deque = collections.deque([(0,k,0)]) 
        print(edges, deque)
        while deque:
            src,dest,time = deque.popleft()
            # append current edge weight+1
            # only when edge not visited
            if (src,time) not in delay:
                delay.append((src,time+1))
                # append all edges starting from dest to deque
                for u,v,w in edges[dest]:
                    deque.append((u,v,w+time))
                print(deque,delay)
        # if not all nodes visited, return -1
        if len(deque) != 0\
            or not delay: return -1
        else: return max(delay)
# Solver.solve(Solution,[[2,1,1],[2,3,1],[3,4,1]],4,2)
# Solver.solve(Solution,[[1,2,1]],2,1)
# Solver.solve(Solution,[[1,2,1]],2,2)
Solver.solve(Solution,[[1,2,1],[2,1,3]],2,2)
