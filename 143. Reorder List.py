# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head and head.next:
            # find the middle point of list
            pre_slow, slow, fast = None, head, head
            while fast and fast.next:
                pre_slow, slow, fast = slow, slow.next, fast.next.next
            if fast:
                pre_slow, slow = slow, slow.next
            pre_slow.next = None
            # reverse the right half list
            previous = None
            while slow:
                slow.next, previous, slow = previous, slow, slow.next
            # merge two half lists
            current = head
            while current and previous:
                current.next, previous.next, current, previous = previous, current.next, current.next, previous.next
                '''
                temp_c = current.next
                temp_p = previous.next
                current.next = previous
                previous.next = temp_c
                current = temp_c
                previous = temp_p
                '''