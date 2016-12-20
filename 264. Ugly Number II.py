class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1] + [0]*(n-1)
        pointers = [0, 0, 0]
        for i in range(1, n):
            ugly[i] = min(ugly[pointers[0]]*2, ugly[pointers[1]]*3, ugly[pointers[2]]*5)
            if ugly[i] == ugly[pointers[0]]*2:
                pointers[0] += 1
            if ugly[i] == ugly[pointers[1]]*3:
                pointers[1] += 1
            if ugly[i] == ugly[pointers[2]]*5:
                pointers[2] += 1
        return ugly[n-1]