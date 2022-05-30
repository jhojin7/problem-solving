from __solver import *
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        op = 0 # number of operations
        print(nums, op, k)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                # if sum of two number is k, then pop both
                print(i,j)
                if nums[i]+nums[j] == k:
                    nums.pop(j)
                    nums.pop(i)
                    # increase op
                    op += 1
        return op


inputs = [
[1,2,3,4]
,5
,[3,1,3,4,3]
,6
]
# Solver.solve(Solution,[1,2,3,4],5)
Solution.maxOperations(Solution,[1,2,3,4],5)
# while inputs:
#     Solver.solve(Solution,inputs.pop(0),inputs.pop(0))