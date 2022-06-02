"""
https://leetcode.com/submissions/detail/712641366/
"""
from __solver import *
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')
Solution().hammingDistance(1,4)
Solution().hammingDistance(3,1)