# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(None)
        current = head
        add = 0
        while l1 and l2:
            val = l1.val+l2.val+add
            if val < 10:
                add = 0
            else:
                val -= 10
                add = 1
            new_node = ListNode(val)
            current.next = new_node
            current = current.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            val = l1.val+add
            if val < 10:
                add = 0
            else:
                val -= 10
                add = 1
            new_node = ListNode(val)
            current.next = new_node
            current = current.next
            l1 = l1.next
        while l2:
            val = l2.val+add
            if val < 10:
                add = 0
            else:
                val -= 10
                add = 1
            new_node = ListNode(val)
            current.next = new_node
            current = current.next
            l2 = l2.next
        if add:
            new_node = ListNode(1)
            current.next = new_node
        return head.next