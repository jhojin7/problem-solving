"""
https://leetcode.com/submissions/detail/701266320/
"""
from __solver import *
class Solution:
    maxlen = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # if end node then return 0
            if not node: return 0
            # dfs tree
            left = dfs(node.left)
            right = dfs(node.right)
            # check children nodes for value
            if node.left and\
                node.val == node.left.val:
                left += 1
            else: left = 0
            if node.right and\
                node.val == node.right.val:
                right += 1
            else: right = 0
            # compare and get maxlen
            self.maxlen = max(self.maxlen,left+right)
            # return self.maxlen
            return max(left,right)
        dfs(root)
        return self.maxlen

arr = [5,4,5,1,1,None,5]
# # arr = [1,4,5,4,4,5]
# root = TreeNode.makeTree(TreeNode,arr)
# TreeNode.printInOrder(TreeNode,root)
# # Solver.solve(Solution,root)
root = \
TreeNode(5,
    TreeNode(4,TreeNode(1),TreeNode(1)),
    TreeNode(5,None,TreeNode(5)))
ret = Solution.longestUnivaluePath(Solution,root)
print(ret)
