"""
https://leetcode.com/submissions/detail/708469173/
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k,nums)[-1]
        return sorted(nums,reverse=True)[k-1]
    