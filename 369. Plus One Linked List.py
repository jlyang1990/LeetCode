# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # reverse
        pre, cur = None, head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        # add one
        add = 1
        pre_tmp, cur_tmp = None, pre
        while cur_tmp:
            val = cur_tmp.val + add
            if val >= 10:
                cur_tmp.val = val%10
                add = 1
            else:
                cur_tmp.val = val
                add = 0
            pre_tmp, cur_tmp = cur_tmp, cur_tmp.next
        if add:
            pre_tmp.next = ListNode(1)
        # reverse
        pre, cur = None, pre
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre