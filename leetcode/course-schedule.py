"""
time limit exceeded. retry later.
https://leetcode.com/submissions/detail/689573063/
https://leetcode.com/submissions/detail/689574353/
"""
from __solver import *

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # init graph
        graph = collections.defaultdict(list)
        for x,y in prerequisites:
            graph[x].append(y)
        # init visited
        visited = set() # set is faster than list() 

        def dfs(cur):
            # if current value is visited, return false
            if cur in visited:
                return False
            visited.add(cur)
            for y in graph[cur]:
                # if 
                if not dfs(y): return False
            visited.remove(cur)
            return True
        for x in list(graph):
            if not dfs(x):
                return False
        return True

inputs = [
2
,[[1,0]]
,2
,[[1,0],[0,1]]
]

# Solver.solve(Solution,4,[[1,0],[2,1],[3,2]])
while inputs:
    Solver.solve(Solution,inputs.pop(0), inputs.pop(0))

# inputs = """
# 2
# [[1,0]]
# 4
# [[1,0],[2,1],[3,2]]
# """
# print(inputs.splitlines(keepends=False))