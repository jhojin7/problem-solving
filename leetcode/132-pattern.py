"""
time limit exceeded
https://leetcode.com/submissions/detail/695548991/
"""
from __solver import * 
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if nums[i] < nums[k] and nums[k] < nums[j]:
                        return True 
        return False

inputs = [
[3,5,0,3,4]
,[1,2,3,4]
,[3,1,4,2]
,[-1,3,2,0]
]

while inputs:
    Solver.solve(Solution, inputs.pop(0))