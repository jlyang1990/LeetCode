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
        if head:
            slow = head
            fast = head
            while fast:
                if not fast.next or fast.next.val != slow.val:
                    slow.next = fast.next
                    slow = slow.next
                fast = fast.next
        return head