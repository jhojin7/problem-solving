"""
https://leetcode.com/submissions/detail/706802453/
"""
from __solver import *
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None
        i = len(nums)//2
        node = TreeNode(nums[i])
        node.left = self.sortedArrayToBST(nums[:i])
        node.right = self.sortedArrayToBST(nums[i+1:])
        return node
nums = [-10,-3,0,5,9]
# nums = [1,3]
root = Solution().sortedArrayToBST(nums)
TreeNode().printInOrder(root)