"""
https://leetcode.com/submissions/detail/707427059/
"""
from __solver import *
class Solution:
    prev = -10**5
    ans = 10**5
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        print(self.ans, root)
        if root.left:
            self.minDiffInBST(root.left)
        self.ans = min(self.ans, root.val - self.prev)
        self.prev = root.val
        if root.right:
            self.minDiffInBST(root.right)
        print(self.ans)
        return self.ans

    def stackInorder(self, root: Optional[TreeNode]) -> int:
        prev = -10**5
        ans = 10**5
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            ans = min(ans, node.val-prev)
            prev = node.val
            node = node.right
        return ans

root = TreeNode().makeTree([1,0,48,None,None,12,49])
root = TreeNode().makeTree([4,2,6,1,3])
print(Solution().minDiffInBST(root) == Solution().stackInorder(root))