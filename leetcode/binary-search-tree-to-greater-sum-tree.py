"""
https://leetcode.com/submissions/detail/707376303/
"""
from __solver import *
class Solution:
    global_sum = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            right = self.bstToGst(root.right)
            self.global_sum += root.val
            print(root.val, self.global_sum)
            root.val = self.global_sum
            left = self.bstToGst(root.left)
        return root

rootList = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
# rootList = [0,None,1]
root = TreeNode().makeTree(rootList)
sol = Solution().bstToGst(root)
TreeNode().printInOrder(sol)