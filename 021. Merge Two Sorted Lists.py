# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            head = l1
            current = head
            current1 = l1.next
            current2 = l2
        else:
            head = l2
            current = head
            current1 = l1
            current2 = l2.next
        while current1 and current2:
            if current1.val < current2.val:
                current.next = current1
                current1 = current1.next
            else:
                current.next = current2
                current2 = current2.next
            current = current.next
        while current1:
            current.next = current1
            current1 = current1.next
            current = current.next
        while current2:
            current.next = current2
            current2 = current2.next
            current = current.next
        return head