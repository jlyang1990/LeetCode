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
        # two pointers
        if not head:
            return head
        slow = head
        fast = head.next
        while fast:
            while fast and fast.val == slow.val:
                fast = fast.next
            slow.next = fast  # automatically set slow.next = None when fast = None
            slow = fast
        return head