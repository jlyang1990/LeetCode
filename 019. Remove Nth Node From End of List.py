# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        current = head
        previous = None
        future = head
        for i in range(n):
            future = future.next
        while future:
            future = future.next
            previous = current
            current = current.next
        if not previous:
            head = current.next
        else:
            previous.next = current.next
        return head