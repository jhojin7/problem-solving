"""
https://leetcode.com/submissions/detail/716363186/
https://leetcode.com/submissions/detail/716315282/
"""
from __solver import *

class Solution:
    def majorityElement(self, nums)->int:
        """ divide and conquer 
        https://leetcode.com/submissions/detail/716368012/ """
        # if len(nums) == 1, return nums
        if len(nums) == 1:
            return nums[0]
        # divide
        left = self.majorityElement(nums[:len(nums)//2])
        right = self.majorityElement(nums[len(nums)//2:])
        # conquer
        # return major elem from left,right
        if nums.count(left) < nums.count(right):
            return right
        else:
            return left

    def dp(self, nums: List[int]) -> int:
        """ dp """
        dp = collections.defaultdict(int)
        for num in nums:
            if not dp[num]:
                dp[num] = nums.count(num)
            if dp[num] > len(nums)//2:
                return num

tc = testcases("""
[3,2,3]
[2,2,1,1,1,2,2]
""")
while tc:
    print(Solution().majorityElement(*tc.popleft()))