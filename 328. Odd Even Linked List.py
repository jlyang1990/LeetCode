# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if head == None or head.next == None, return head directly
        if head and head.next:
            odd_head = odd = head
            even_head = even = head.next
            current = head.next.next
            while current and current.next:
                odd.next = current
                odd = odd.next
                even.next = current.next
                even = even.next
                current = current.next.next
            if current:
                odd.next = current
                odd = odd.next
                even.next = None
            head = odd_head
            odd.next = even_head
        return head