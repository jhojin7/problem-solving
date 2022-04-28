'''
https://leetcode.com/submissions/detail/689105473/
'''
from __solver import *
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(sum, path, idx):
            # backtrack if sum of the path gets below 0
            if sum<0: return
            # append and backtrack if sum is 0 
            if sum == 0:
                result.append(path)
                return
            for i in range(idx, len(candidates)):
                dfs(sum-candidates[i], path+[candidates[i]], i)# not idx here
        result = []
        # start from sum=target and subtract from target until 0
        dfs(target,[],0)
        return result
        


inputs = collections.deque([
[2,3,6,7]
,7
,[2,3,5]
,8
,[2]
,1
])

# Solver.solve(Solution,inputs[-2],inputs[-1])
while inputs:
    Solver.solve(Solution,
        inputs.popleft(), inputs.popleft())


# ins ="""[2,3,6,7]
# 7
# [2,3,5]
# 8
# [2]
# 1""".split('\n')
# print(type(ins[0].strip()))