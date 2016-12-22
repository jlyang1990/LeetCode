# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = ListNode(None)
        current = new_head
        pre, cur = None, head
        while cur:
            if (not cur.next or cur.next.val != cur.val) and (not pre or pre.val != cur.val):
                current.next = cur
                current = current.next
            pre, cur = cur, cur.next
        current.next = None  # don't forget!
        return new_head.next