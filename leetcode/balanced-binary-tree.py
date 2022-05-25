"""
https://leetcode.com/submissions/detail/706673724/
"""
from __solver import *
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node: 
                return 0
            left = check(node.left)
            right = check(node.right)
            if abs(left-right)>1\
                or left==-1 or right==-1:
                return -1
            else:
                return max(left,right)+1
        return (-1 != check(root))

root = TreeNode().makeTree([3,9,20,None,None,15,7])
root = TreeNode().makeTree([1,2,2,3,3,None,None,4,4])
# root = TreeNode().makeTree([])
TreeNode().printInOrder(root)
print(Solution().isBalanced(root))