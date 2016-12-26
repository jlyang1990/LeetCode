# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        head = ListNode(None)
        current = head
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))
        while heap:
            _, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))
        return head.next