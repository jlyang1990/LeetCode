class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # O(n) time, O(1) space
        if len(A) < 3:
            return 0
        count = 0
        start = 0
        diff = A[1] - A[0]
        for i in range(1, len(A)):
            if A[i] - A[i-1] != diff:
                count += (i-start-1)*(i-start-2)/2
                start = i-1
                diff = A[i] - A[i-1]
        # last possible arithmatic slices
        count += (len(A)-start-1)*(len(A)-start-2)/2
        return count