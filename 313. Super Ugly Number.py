class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        # k pointers
        # O(nk) time, O(n+k) space
        pointer = [0]*len(primes)
        ugly = [1]+[float("inf")]*(n-1)
        for i in range(1, n):
            for j in range(len(primes)):
                ugly[i] = min(ugly[i], ugly[pointer[j]]*primes[j])
            for j in range(len(primes)):
                if ugly[i] == ugly[pointer[j]]*primes[j]:
                    pointer[j] += 1
        return ugly[n-1]