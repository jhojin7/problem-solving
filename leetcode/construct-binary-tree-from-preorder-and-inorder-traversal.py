"""
https://leetcode.com/submissions/detail/707806807/
"""
from __solver import *
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        print(preorder, inorder)
        # if list empty, return None
        if not preorder or not inorder:
            return None
        # first element in preorder is root
        val = preorder.pop(0)
        if val in inorder:
            idx = inorder.index(val)
        else: # if val not in inorder, return none
            return None
        # make node and build child nodes
        node = TreeNode(inorder[idx])
        node.left = self.buildTree(preorder, inorder[0:idx])
        node.right = self.buildTree(preorder, inorder[idx+1:])
        return node

# preorder, inorder = [-1],[-1]
# preorder, inorder = [3,9,20,15,7],[9,3,15,20,7]
preorder, inorder = [1,2,4,5,3,6,7,9,8],[4,2,5,1,7,9,6,8,3]
TreeNode().printInOrder(Solution().buildTree(preorder,inorder))