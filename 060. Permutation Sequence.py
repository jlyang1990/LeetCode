class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # O(n^2) time, O(n) space
        result = ""
        nums = list(range(1, n+1))
        factorial = 1
        for i in range(1, n):
            factorial *= i  # factorial = (n-1)!
        k -= 1
        for i in range(n-1, -1, -1):
            index = k//factorial
            result = result+str(nums[index])
            del nums[index]
            k -= index*factorial
            if i != 0:
                factorial /= i
        return result