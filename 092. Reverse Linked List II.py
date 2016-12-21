# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head and head.next:
            current = head
            previous = None
            for i in range(m-1):
                current, previous = current.next, current
            current_m = current
            previous_m = previous
            current, previous = current.next, current
            for i in range(n-m):
                current.next, previous, current = previous, current, current.next  # the order matters!
            current_m.next = current
            if not previous_m:
                head = previous
            else:
                previous_m.next = previous
        return head