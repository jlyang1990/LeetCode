# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre_slow, slow, fast = None, head, head
        while fast and fast.next:
            pre_slow, slow, fast = slow, slow.next, fast.next.next
        pre_slow.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return self.mergeTwoLists(l1, l2)
        
    def mergeTwoLists(self, l1, l2):
        head = ListNode(None)
        current = head
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        while l1:
            current.next = l1
            l1 = l1.next
            current = current.next
        while l2:
            current.next = l2
            l2 = l2.next
            current = current.next
        return head.next