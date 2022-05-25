"""
https://leetcode.com/submissions/detail/706742939/
"""
from __solver import *
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n<=1: return [0]
        graph = collections.defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        to_del = [node for node in range(n) if len(graph[node]) == 1]
        while n>2:
            n -= len(to_del)
            new_to_del = []
            for b in to_del:
                a = graph[b].pop()
                graph[a].remove(b)
                if len(graph[a])==1:
                    new_to_del.append(a)
            to_del = new_to_del
        return (to_del)

n,edges = 4,[[1,0],[1,2],[1,3]]
print(Solution().findMinHeightTrees(n,edges))
n,edges = 6,[[3,0],[3,1],[3,2],[3,4],[5,4]]
n,edges = 1,[]
n,edges = 2,[[0,1]]