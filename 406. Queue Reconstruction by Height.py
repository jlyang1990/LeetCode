class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # O(n^2) time
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        result = []
        for p in people:
            result.insert(p[1], p)
        return result