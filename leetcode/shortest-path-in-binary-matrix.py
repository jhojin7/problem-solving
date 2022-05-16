"""
https://leetcode.com/submissions/detail/700563815/
https://11001.tistory.com/m/77
"""
from __solver import *
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = [(0,0,1)] #i,j,pathlen

        # if start or end point ==1, return
        if grid[0][0] == 1\
            or grid[len(grid)-1][len(grid)-1] == 1: 
            return -1

        # bfs
        while q: 
            i,j,pathlen = q.pop(0)
            # if at destination, stop loop and return pathlen
            if i==len(grid)-1 and j==len(grid)-1:
                return pathlen
            grid[i][j] = -1 # mark as visited
            # for movements in [N,NE,E,SE,S,SW,W,NW](in different order)
            for a,b in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                # append to queue
                if i+a<len(grid) and j+b<len(grid[0])\
                    and 0<=i+a and 0<=j+b\
                    and grid[i+a][j+b]==0:
                    print((i+a,j+b,pathlen+1))
                    q.append((i+a,j+b,pathlen+1))
        # if no clear path, return -1
        return -1
grid = [[0,0,0],[1,1,0],[1,1,1]]
grid = [[0,1,1,0,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,1,1,0],[1,1,1,1,0]]
grid = [[0,1,1,0,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,1,1,0],[1,1,1,1,0]]
    # def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    #     print(grid)
    #     def dfs(grid,i,j):
    #         print(grid[i][j])
    #         # if current pos is out of grid
    #         if i>=len(grid) and j>=len(grid[0]):
    #             return -1
    #         # check all other paths and find max out of them 
    #         east = dfs(grid,i,j+1)
    #         southeast = dfs(grid,i+1,j+1)
    #         south = dfs(grid,i+1,j)
    #         self.pathlen = max(self.pathlen,east,southeast,south)
    #         print(self.pathlen)

    #     # if starting point == 1, return
    #     if grid[0][0] == 1: return -1
    #     # do dfs
    #     dfs(grid,0,0)
    #     return self.pathlen
# grid = [[0,1],[1,0]]
# grid = [[0,0,0],[1,1,0],[1,1,0]]
# grid = [[1,0,0],[1,1,0],[1,1,0]]
Solver.solve(Solution,grid)
        