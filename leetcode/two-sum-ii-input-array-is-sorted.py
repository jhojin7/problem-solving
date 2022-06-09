"""
https://leetcode.com/submissions/detail/717755264/
https://leetcode.com/submissions/detail/711797500/
https://leetcode.com/submissions/detail/711805432/
"""
from __solver import *
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for k,v in enumerate(numbers):
        #     expected = target-v
        #     nums = numbers[k+1:]
        #     i = bisect.bisect_left(nums, expected)
        #     if i<len(nums) and numbers[i+k+1] == expected:
        #         return [k+1,i+k+2]


        print(numbers, target)
        l, r = 0, len(numbers)-1
        while l<len(numbers) and r>=0:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                return (l+1,r+1)
        return -1

tc = testcases("""
[2,7,11,15]
9
[2,3,4]
6
[-1,0]
-1
[1,2,5,6,6,7,7,8,8,9,9,9,9,19,29,39]
40
""",2)
while tc:
    print(Solution().twoSum(*tc.popleft()))