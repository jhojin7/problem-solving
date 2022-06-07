"""
https://leetcode.com/submissions/detail/716624495/ 181ms
https://leetcode.com/submissions/detail/716637624/ 125ms
"""
from __solver import *
class Solution:
    def NOTfindMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # print(nums1, nums2)
        # not log(m+n) time...?
        nums = sorted(nums1+nums2)
        if len(nums)%2 == 0:
            return sum(nums[len(nums)//2-1
                        :len(nums)//2+1])/2
        else:
            return (nums[len(nums)//2])

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # print(nums1, nums2)
        merged = []
        i, j, k = 0, 0, 0
        m, n = len(nums1), len(nums2)
        # modified merge sort
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merged.insert(k, nums1[i])
                i, k = i+1, k+1
            else:
                merged.insert(k, nums2[j])
                j, k = j+1, k+1
        while i < m:
            merged.insert(k, nums1[i])
            i, k = i+1, k+1
        while j < n:
            merged.insert(k, nums2[j])
            j, k = j+1, k+1
        # print(merged)

        # find median
        mid = len(merged)//2
        # if merged len is even
        if len(merged) % 2 == 0:
            return sum(merged[mid-1:mid+1])/2
        # if merged len is odd:
        else:
            return merged[mid]

tc = testcases("""
[1,3]
[2]
[1,2]
[3,4]
[1,2,7,8,9,1998,1998]   
[3,4,5,6]
""",2)
# while tc:
#     sol = Solution().findMedianSortedArrays(*tc.pop())
#     print(">>> ",sol)

import timeit
args = tc.pop()
print(len(args[0]),len(args[1])) # 968 968
t1 = timeit.timeit("""Solution().NOTfindMedianSortedArrays(*args)""",globals=globals(),number=5000)
t2 = timeit.timeit("""Solution().findMedianSortedArrays(*args)""",globals=globals(),number=5000)
print(t1,t2) 
# 0.8461176 2.3398296999999997
# 0.6933286 2.5510639