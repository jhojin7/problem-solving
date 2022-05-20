"""
https://leetcode.com/submissions/detail/703358795/
"""
from __solver import *
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            print(root1.val + root2.val)
            root3 = TreeNode(root1.val + root2.val)
            root3.left = self.mergeTrees(self,root1.left, root2.left)
            root3.right = self.mergeTrees(self,root1.right, root2.right)
            return root3
        else: # if not(root1 and root2)
            return root1 or root2
        #     if root1.left and root2.left:
        #         print(root1.left.val, root2.left.val)
        #         root3.left = self.mergeTrees(self, root1.left, root2.left)
        #     if root1.right and root2.right:
        #         print(root1.right.val, root2.right.val)
        #         root3.right = self.mergeTrees(self, root1.right, root2.right)
        # return root3
        
# [1,3,2,5]
# [2,1,3,null,4,null,7]
# [1]
# [1,2]
root1 = TreeNode.makeTree(TreeNode,[1,3,2,5])
TreeNode.printInOrder(TreeNode,root1)
root2 = TreeNode.makeTree(TreeNode,[2,1,3,None,4,None,7])
TreeNode.printInOrder(TreeNode,root2)
print("\n")

root3 =Solution.mergeTrees(Solution,root1, root2)
TreeNode.printInOrder(TreeNode,root3)

