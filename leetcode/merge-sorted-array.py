"""
https://leetcode.com/submissions/detail/716290946/
"""
from __solver import *

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1, m = [0], 0
        # nums2, n = [1], 1
        print(nums1,m,nums2,n)
        # if nums1 is empty, get nums2 to nums1
        if m == 0:
            # nums1.clear()
            # nums1 = nums2.copy()
            nums1[:] = nums2
            pass
        # if nums2 is empty, nums1 is sorted
        elif n == 0:
            pass
        # copy nums2 to nums1
        nums1[m:] = nums2
        print(nums1)
        # sort
        for i in range(m+n):
            for j in range(i,m+n):
                if nums1[i] > nums1[j]:
                    nums1[i], nums1[j] = \
                        nums1[j], nums1[i]
        print("return ",nums1)

tc = testcases("""
[4,0,0,0,0,0]
1
[1,2,3,5,6]
5
[1,2,3,0,0,0]
3
[2,5,6]
3
[1]
1
[]
0
[0]
0
[1]
1
[2,4,6,8,0,0,0,0,0]
4
[1,3,5,7,9]
5
""",4)
# Solution().merge(*tc[0])
while tc:
    args = tc.popleft()
    Solution().merge(*args)