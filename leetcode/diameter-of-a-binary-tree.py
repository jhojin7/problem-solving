"""
https://leetcode.com/submissions/detail/700524247/
"""
from __solver import *
class Solution:
    maxlen = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return -1
            lenL = dfs(node.left)
            lenR = dfs(node.right)
            self.maxlen = max(self.maxlen,lenL+lenR+2) 
            return max(lenL,lenR)+1
        dfs(root)
        print(self.maxlen)
        return self.maxlen
root = TreeNode(1,TreeNode(2),None)
# root = TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3))
Solution.diameterOfBinaryTree(Solution,root)