"""
https://leetcode.com/submissions/detail/690263392/
"""
from __solver import *
# [4,2,1,3]
# [-1,5,3,4,0]
# []
# input = ListNode(4,ListNode(2,ListNode(1,ListNode(3,None))))
# # input = ListNode(-1,ListNode(5,ListNode(3,ListNode(4,ListNode(0,None)))))
# print(Solution.sortList(Solution,input))

class Solution:
    def mergeLists(self, l1, l2):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeLists(l1.next, l2)
        return l1 or l2
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if node = None
        if not (head and head.next):
            return head
        # pointers
        slow, fast = head, head
        half = None
        # while fast and next exists
        while fast and fast.next:
            half = slow
            slow, fast = slow.next, fast.next.next
        half.next = None
        
        # divide and conquer
        l1 = self.sortList(head)
        l2 = self.sortList(slow) 
        return self.mergeLists(l1, l2)