"""
https://leetcode.com/submissions/detail/699927505/
"""
from __solver import *
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # bfs
        # tmpSum = sum of all nodes in that level
        # if last level(empty deque after loop), return tmpSum
        deque = collections.deque([root])
        tmpSum = 0
        while deque:
            tmpSum = 0
            for _ in range(len(deque)):
                node = deque.popleft()
                tmpSum += node.val
                print(node.val, tmpSum)
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
            print("end level")
        print(tmpSum)
        return tmpSum
            
            
        # deepestLeaves = []
        # print(root)
        # def dfs(node:TreeNode,partSum:int):
        #     print(node.val, partSum)
        #     if not node.left and not node.right:
        #         deepestLeaves.append(node.val)
        #     if node.left: dfs(node.left,partSum+node.val)
        #     if node.right: dfs(node.right,partSum+node.val)
        # summ = dfs(root,0)
        # print(sum(deepestLeaves))
        # pass

# [1,2,3,4,5,null,6,7,null,null,null,null,8]
# [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
root = [1,2,3,4,5,None,6,7,None,None,None,None,8]
root = [6,7,8,2,7,1,3,9,None,1,4,None,None,None,5]
root = \
TreeNode(1,
    TreeNode(2,
        TreeNode(4,
            TreeNode(7),
            None),
        TreeNode(5)),
    TreeNode(3,
        None,
        TreeNode(6,
            None,
            TreeNode(8))))
root = \
TreeNode(6,
    TreeNode(7,
        TreeNode(2,
            TreeNode(9),None),
        TreeNode(7,
            TreeNode(1),TreeNode(4))),
    TreeNode(8,
        TreeNode(1),
        TreeNode(3,
            None,TreeNode(5))))
Solution.deepestLeavesSum(Solution,root)