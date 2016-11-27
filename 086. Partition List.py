# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        current = head
        smaller = None
        smaller_head = None
        larger = None
        larger_head = None
        while current:
            if current.val < x:
                if smaller:
                    smaller.next = current
                    smaller = smaller.next
                else:
                    smaller = current
                    smaller_head = smaller
            else:
                if larger:
                    larger.next = current
                    larger = larger.next
                else:
                    larger = current
                    larger_head = larger
            current = current.next
        if smaller:
            head = smaller_head
            smaller.next = larger_head
            if larger:
                larger.next = None
        return head