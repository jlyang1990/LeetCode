# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        current = head
        length = 0
        while current:
            current = current.next
            length +=1
        k = k % length
        if k == 0:
            return head
        pre_fast, fast = None, head
        while k > 0:
            pre_fast, fast = fast, fast.next
            k -= 1
        pre_slow, slow = None, head
        while fast:
            pre_slow, slow, pre_fast, fast = slow, slow.next, fast, fast.next
        pre_fast.next = head
        pre_slow.next = None
        return slow