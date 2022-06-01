"""
https://leetcode.com/submissions/detail/711968290/
"""
from operator import le
from __solver import *
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find pivot
        pivot = nums.index(min(nums))
        # binary search
        left,right = 0,len(nums)-1
        mid = -999999
        while left<=right:
            # calculate new mid and its pivot
            mid = left+(right-left)//2
            mid_pivoted = (mid+pivot)%len(nums)
            print(left,mid_pivoted,right)
            # set new left,right,return
            if nums[mid_pivoted] < target:
                left = mid+1
            elif nums[mid_pivoted] > target:
                right = mid-1
            else:
                return mid_pivoted
        # if no target
        return -1

    def notsearch(self, nums: List[int], target: int) -> int:
        # find pivot
        pivot = nums.index(min(nums))
        # # print with pivoted_i
        # for i in range(len(nums)):
        #     pivoted_i = (i+pivot)%len(nums)
        #     print(pivoted_i, nums[pivoted_i])
        
        # binary search
        left = (0+pivot)%len(nums)
        right = (len(nums)-1+pivot)%len(nums)
        # mid = ((left+(right-left))//2+pivot)%len(nums)
        # left,right = 0,len(nums)-1
        mid = (left+(right-left))//2
        # mid_pivoted = (mid+pivot)%len(nums)
        print(left,mid,right)

        for _ in range(len(nums)):
        # while (left*len(nums)-pivot) < (right*len(nums)-pivot):
            mid = (left+(right-left))//2
            # mid_pivoted = (mid+pivot)%len(nums)
            # mid = ((left+(right-left))//2+pivot)%len(nums)
            print(left,mid,right)
            if nums[mid] > target:
                # right = mid-1
                right = (mid-1+pivot)%len(nums)
            elif nums[mid] < target:
                # left = mid
                left = (mid+pivot)%len(nums)
            else: # nums[mid] == target:
                return mid
        # if no target in nums
        return -1

# nums, target = [4,5,6,7,0,1,2],0
nums, target = [4,5,6,7,0,1,2],3
# nums, target = [1],0
print(Solution().search(nums, target))