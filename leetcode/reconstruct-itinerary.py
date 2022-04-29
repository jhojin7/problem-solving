"""
https://leetcode.com/submissions/detail/689535683/
"""
from __solver import *

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        visited = []
        # define a dict with list
        routes = collections.defaultdict(list)
        # traverse all tickets and append all routes as src:[dest,dest]
        for src,dest in sorted(tickets):
            routes[src].append(dest)
        def dfs(src):
            # for all dest in src
            while routes[src]:
                dfs(routes[src].pop(0))
            # visit in reversed order
            visited.append(src)
        
        # start from JFK (given)
        dfs('JFK')
        return visited[::-1] # return reversed list

inputs = [
[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
,[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
]
for input in inputs:
    Solver.solve(Solution,input)