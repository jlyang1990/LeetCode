# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        import gc
        gc.collect()
        pA = headA
        pB = headB
        countA = 0
        countB = 0
        while pA:
            countA += 1
            pA = pA.next
        while pB:
            countB += 1
            pB = pB.next
        pA = headA
        pB = headB
        if countA - countB > 0:
            for i in range(countA - countB):
                pA = pA.next
        if countB - countA > 0:
            for i in range(countB - countA):
                pB = pB.next
        while pA != pB:
            pA = pA.next
            pB = pB.next
        return pA