'''
https://leetcode.com/submissions/detail/689113203/
'''
from __solver import *

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(idx, path):
            # all paths are needed. no backtracking
            result.append(path)
            # for every num, go one depth deeper
            for i in range(idx,len(nums)): 
                # move i forward every loop
                dfs(i+1,path+[nums[i]])
        result = []
        dfs(0,[])
        return result

inputs = [
[1,2,3]
,[0]
]
Solver.solve(Solution,inputs[1])