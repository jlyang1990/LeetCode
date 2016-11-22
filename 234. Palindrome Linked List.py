# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rev, slow, fast = None, head, head
        while fast and fast.next:
            fast = fast.next.next
            slow, rev, rev.next = slow.next, slow, rev
        if fast:
            slow = slow.next  # odd number of nodes, jump the node in the middle
        while rev and slow:
            if rev.val != slow.val:
                return False
            rev, slow = rev.next, slow.next
        return True