"""
https://leetcode.com/submissions/detail/703498350/
https://leetcode.com/submissions/detail/703532478/
https://leetcode.com/problems/unique-paths-ii/discuss/2055409/Beginner-Friendly-"Recursion-to-DP"-Intuition-Explained-Python
"""
from __solver import *
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        # m*n arr for memoization
        # 
        visited = [[-1]*n for _ in range(m)]
        # print(visited)
        # if start and fin have 1, return 0
        if obstacleGrid[0][0]==1 or obstacleGrid[-1][-1]==1:
            return 0
        # dfs 
        # if gridxy is obstacle or edge,
        # return 0
        # if end return 1
        # return dfs(right)+dfs(down)

        def dfs(grid,x,y):
            # if bottom-left, cnt+1
            if x==m-1 and y==n-1:
                return 1
            # if edge or obstacle
            if m<=x or n<=y or grid[x][y] == 1:
                return 0
            # if already visited
            if visited[x][y] != -1:
                return visited[x][y]
            # return dfs(down)+dfs(right)
            # print(x,y,visited[x][y])
            visited[x][y] = dfs(grid,x+1,y) + dfs(grid,x,y+1)
            return visited[x][y] 

        # do dfs
        ret = dfs(obstacleGrid,0,0)
        print(ret)
        return ret

gridd = [[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,0]]
gridd = [[0,0,0],[0,0,0],[0,0,0]]
gridd = [[0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0],[1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0],[1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],[0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],[0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1],[0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],[1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0],[0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,1,1,0],[0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1],[0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0],[1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0],[1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1],[1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0]]
Solution.uniquePathsWithObstacles(Solution,gridd)