"""
https://leetcode.com/submissions/detail/707386269/
"""
from __solver import *
class Solution:
    def dfsPruning(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node: return 0
            if node.val<low: return dfs(node.right)
            elif node.val>high: return dfs(node.left)
            print(node.val)
            return node.val + dfs(node.left) + dfs(node.right)
        return dfs(root)

    def dfsStack(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        sum = 0
        while stack:
            node = stack.pop()
            if node:
                print(node.val)
                if node.val > low: stack.append(node.left)
                elif node.val < high: stack.append(node.right)

                if low <= node.val <= high:
                    sum += node.val
        return sum

    def bfsQueue(self, root: Optional[TreeNode], low: int, high: int) -> int:
        queue = collections.deque([root])
        sum = 0
        while queue:
            node = queue.popleft()
            if node:
                print(node.val)
                if node.val > low: queue.append(node.left)
                elif node.val < high: queue.append(node.right)

                if low <= node.val <= high:
                    sum += node.val
        return sum

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root:
            nodeSum = 0
            if low <= root.val <= high:
                nodeSum = root.val
                print(root.val)
            lSum = self.rangeSumBST(root.left,low,high)
            rSum = self.rangeSumBST(root.right,low,high)
            return nodeSum + lSum + rSum
        # if leaf node
        return 0
# root = TreeNode().makeTree([10,5,15,3,7,None,18])
# print(Solution().rangeSumBST(root,7,15))
root = TreeNode().makeTree([10,5,15,3,7,13,18,1,None,6])
# print(Solution().rangeSumBST(root,6,10) == Solution().dfsPruning(root,6,10))
# print(Solution().rangeSumBST(root,6,10) == Solution().dfsStack(root,6,10))
print(Solution().rangeSumBST(root,6,10) == Solution().bfsQueue(root,6,10))
