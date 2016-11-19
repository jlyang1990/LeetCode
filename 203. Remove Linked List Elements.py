# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        current = head
        previous = None
        while not current:
            if current.val == val:
                if previous == None:
                    head = current.next
                else:
                    previous.next = current.next
            else:
                previous = current
            current = current.next
        return head