# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = ListNode(None)
        pointer = new_head
        current = head
        while current:
            while pointer.next and pointer.next.val < current.val:
                pointer = pointer.next
            current.next, pointer.next, current, pointer = pointer.next, current, current.next, new_head
            '''
            temp = current.next
            current.next = pointer.next
            pointer.next = current
            current = current.next
            pointer = new_head
            '''
        return new_head.next