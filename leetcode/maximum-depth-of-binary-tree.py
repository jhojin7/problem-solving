"""
https://leetcode.com/submissions/detail/698578866/
"""
from __solver import *
# import math
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if no input, return 0
        if not root: return 0
        # deque to store nodes. 
        deque = collections.deque([root])
        depth = 0
        while deque:
            depth += 1
            # for node in deque:
            for _ in range(len(deque)): # do not traverse through all elems
                node = deque.popleft()
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
        return depth

        """dfs는 깊이를 구하기엔 안맞나..?"""
        # def count_nodes(node):
        #     self.depth += 1
        #     if node.left: count_nodes(node.left)
        #     if node.right: count_nodes(node.right)
        # count_nodes(root)
        # print(self.depth)

        # def count_nodes(node):
        #     if not node: nodes.append(-1)
        #     else: 
        #         nodes.append(node.val)
        #         self.depth += 1
        #         count_nodes(node.left)
        #         count_nodes(node.right)

        # nodes = []
        # if not root: return 0
        # count_nodes(root)
        # print(nodes, math.ceil(len(nodes)/2))
        # print(self.depth)
        # return len(nodes)//2+1

        # def dfs(depth,node):
        #     print("visit",node.val,"depth",depth)
        #     # if depth > max: max = depth
        #     if node.left: 
        #         dfs(depth+1,node.left)
        #     if node.right:
        #         dfs(depth+1,node.right)
        # # max = 0
        # dfs(1,root)
        # print("depth",max)
        # return max

# [3,9,20,null,null,15,7]
# [1,null,2]
# []
# [1,2,null,3,null,4,null,5]

root = TreeNode(1,TreeNode(2,TreeNode(3,TreeNode(4,TreeNode(5),None),None),None),None)

root = \
    TreeNode(1,
        None,
        TreeNode(2))

root = \
    TreeNode(3,
        TreeNode(9),
        TreeNode(20,
            TreeNode(15),TreeNode(7)))
Solver.solve(Solution,root)

arr = [3,9,20,None,None,15,7]
tree = TreeNode.makeTree(TreeNode,arr)
# TreeNode.printInOrder(TreeNode,tree)
Solver.solve(Solution,tree)