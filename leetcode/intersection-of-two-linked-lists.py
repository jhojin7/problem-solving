"""
https://leetcode.com/submissions/detail/715408091/
https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/2116428/Python-An-Easy-Approach
"""
from __solver import *
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # nodeA, nodeB = headA, headB
        # nodesA,nodesB = [],[]
        # while nodeA:
        #     nodesA.append(nodeA)
        #     nodeA = nodeA.next
        # while nodeB:
        #     nodesB.append(nodeB)
        #     nodeB = nodeB.next
        # for a in nodesA:
        #     for b in nodesB:
        #         if a==b:
        #             return a.val
        # return None
        nodeA, nodeB = headA, headB
        setA = set()
        while nodeA:
            setA.add(nodeA)
            nodeA = nodeA.next
        while nodeB:
            if nodeB in setA:
                return nodeB
            nodeB = nodeB.next
        return None
# 8
intersectNode = ListNode(8,ListNode(4,ListNode(5)))
headA = ListNode(4,ListNode(1,intersectNode))
headB = ListNode(5,ListNode(6,ListNode(1,intersectNode)))

# # None
# headA = ListNode(2,ListNode(6,ListNode(4)))
# headB = ListNode(1,ListNode(5))

# # 2
# intersect = ListNode(2,ListNode(4))
# headA = ListNode(1,ListNode(9,ListNode(1,intersect)))
# headB = ListNode(3,intersect)

print("ret",Solution().getIntersectionNode(headA, headB).val)