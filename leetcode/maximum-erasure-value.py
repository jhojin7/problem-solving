"""
https://leetcode.com/submissions/detail/720213934/
"""
from __solver import *
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        subarr = set()
        # use subsum to not sum() every loop
        subsum, maxsum = 0, 0
        left, right = 0, 0
        
        while right < len(nums):
            # if right ptr not in set, add and move ptr
            if nums[right] not in subarr:
                subarr.add(nums[right])
                subsum += nums[right]
                right += 1
            # else, remove and move left ptr
            else:
                subarr.remove(nums[left])
                subsum -= nums[left]
                left += 1
            maxsum = max(subsum, maxsum)
        return maxsum


# [4,2,4,5,6]
# [5,2,1,2,5,2,1,2,5]
tc = testcases("""
[187,470,25,436,538,809,441,167,477,110,275,133,666,345,411,459,490,266,987,965,429,166,809,340,467,318,125,165,809,610,31,585,970,306,42,189,169,743,78,810,70,382,367,490,787,670,476,278,775,673,299,19,893,817,971,458,409,886,434]
""")
while tc:
    print(Solution().maximumUniqueSubarray(*tc.popleft()))