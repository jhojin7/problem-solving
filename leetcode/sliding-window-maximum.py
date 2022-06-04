"""
"""
from __solver import *
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = collections.deque([])
        ans = []
        cur_max = -math.inf

        # append k elems
        for i,val in enumerate(nums):
            window.append(val)
            if i<k-1: continue

            # set cur_max
            if cur_max == -math.inf:
                cur_max = max(window)
            elif val > cur_max:
                cur_max = val
            ans.append(cur_max)
            # if popped==cur_max, reset max
            if cur_max == window.popleft():
                cur_max = -math.inf
        return ans

nums, k = [1,3,-1,-3,5,3,6,7],3
# nums, k = [1],1
print(Solution().maxSlidingWindow(nums, k))