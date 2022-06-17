"""
ac:https://leetcode.com/submissions/detail/724146741/
https://leetcode.com/problems/binary-tree-cameras/discuss/211412/C++-DFS-simplest
"""
from __solver import *
class Solution:
    cnt = 0
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # if node==None
            if not node: return -1
            # dfs child
            left = dfs(node.left)
            right = dfs(node.right)
            print(node, left, right)
            # if children no have cam, i need one
            if left == 0 or right == 0:
                self.cnt += 1
                return 1
            # if children has cam, i dont need one
            elif left == 1 or right == 1: 
                return -1
            else: 
                return 0

        # if root returns no cam, add one
        if dfs(root) == 0:
            self.cnt += 1
        return self.cnt

root = BinaryTree().makeTree([0,0,None,0,0])
root = BinaryTree().makeTree([0,0,None,0,None,0,None,None,0])
print(Solution().minCameraCover(root))