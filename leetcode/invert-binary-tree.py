"""
https://leetcode.com/submissions/detail/701870316/
"""
from __solver import *
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left = self.invertTree(self,root.right)
            root.right = self.invertTree(self,root.left)
            return root
        return None
    
    def my_invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # https://leetcode.com/submissions/detail/701870316/
        def levelOrder(new_node, node):
            if not node or not new_node: return
            print(node.val, new_node.val)
            if node.right:
                new_node.left = TreeNode(node.right.val)
            if node.left:
                new_node.right = TreeNode(node.left.val)
            levelOrder(new_node.left,node.right)
            levelOrder(new_node.right,node.left)
        # main
        new_root = TreeNode(root.val,None,None)
        levelOrder(new_root, root)
        # try printing levelorder
        TreeNode.printInOrder(TreeNode,new_root)
        print("inorder")
        return new_root



input = [4,2,7,1,3,6,9]
# input = [2,1,3]
# input =[]
root = TreeNode.makeTree(TreeNode,input)
# Solver.solve(Solution,"invertTree",root)
new_root = Solution.invertTree(Solution,root)
TreeNode.printInOrder(TreeNode,new_root)