# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = head
        for i in range(n):
            dummy = dummy.next
        if not dummy:
            return head.next
        curr = head
        while dummy.next is not None:
            curr = curr.next
            dummy = dummy.next
        curr.next = curr.next.next
        return head
