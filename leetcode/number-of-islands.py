'''
https://leetcode.com/submissions/detail/687763134/
'''
from typing import * 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i:int, j:int):
            # size = 0
            # # if not in map or is water, return
            # in_map = (i>0 and i<=len(grid) 
            #     and j>0 and j<=len(grid[0]))
            # is_water = (grid[i][j] == '0')
            # if not in_map or is_water: return 0
            if i < 0 or i >= len(grid)\
                or j < 0 or j >= len(grid[0])\
                or grid[i][j] != '1':
                return
            # else, visit
            grid[i][j] = '0' # mark land as water
            # and do recursive dfs
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i,j+1)
            # return size

        cnt = 0
        # for every grid on map
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # if land, do dfs
                if grid[i][j] == '1':
                    dfs(i,j)
                    cnt += 1
        return cnt

        

inputs =[
[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
,[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
]

for input in inputs:
    output = Solution.numIslands(Solution,grid=input)
    print('>> ', input, '\n', output)