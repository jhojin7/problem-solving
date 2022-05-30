"""
https://leetcode.com/submissions/detail/710638264/
"""
<<<<<<< HEAD
from calendar import LocaleHTMLCalendar
from threading import local
=======
>>>>>>> 1212ba85779c9314713ad1ec4e6499a3a9029e80
from __solver import *
class Solution:
    def mergeTwoLists(self, l1,l2):
        if l1 and l2:
            if l1.val > l2.val:
                l1,l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head
        # find half point with runner
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        # break link in half node
        half.next = None
        # merge sort
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return self.mergeTwoLists(l1,l2)
<<<<<<< HEAD
    
    def localSortlist(self,head:ListNode):
        node = head
        arr = []
        while node:
            arr.append(node.val)
            node = node.next
        arr.sort()
        node = head
        for i in range(len(arr)):
            node.val = arr[i]
            node = node.next
        return head

            

head = ListNode(3,ListNode(5,ListNode(4,ListNode(2,ListNode(1)))))
# solhead = Solution().sortList(head)
# while solhead:
#     print(solhead.val)
#     solhead = solhead.next

localhead = Solution().localSortlist(head)
while localhead:
    print(localhead.val)
    localhead = localhead.next
=======

head = ListNode(3,ListNode(5,ListNode(4,ListNode(2,ListNode(1)))))
solhead = Solution().sortList(head)
while solhead:
    print(solhead.val)
    solhead = solhead.next
>>>>>>> 1212ba85779c9314713ad1ec4e6499a3a9029e80
