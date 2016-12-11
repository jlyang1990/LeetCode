class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        # O(n^2) time, O(n^2) space
        dic = {}
        count = 0
        for i in A:
            for j in B:
                if i+j not in dic:
                    dic[i+j] = 1
                else:
                    dic[i+j] += 1
        for i in C:
            for j in D:
                if -i-j in dic:
                    count += dic[-i-j]
        return count