# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        # return a random node's value in one run
        # Reservior Sampling
        from random import random
        random_val = self.head.val
        current = self.head.next
        count = 0
        while current:
            count += 1
            if random() < 1.0/(1+count):
                random_val = current.val
            current = current.next
        return random_val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()