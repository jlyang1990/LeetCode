class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # An increasingly sorted array a[1...n]
        # L[n]: the length of the largest divisible subset whose largest number is a[n]
        # L[n+1] = max_{1<=i<=n} 1+L[i] if a[n+1]%a[i] = 0 else 1
        # O(n^2) time, O(n) space
        if len(nums) == 0:
            return []
        nums.sort()
        n = len(nums)
        L = [1]*n
        pre = range(n)
        maxL = 1
        maxpre = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and 1 + L[j] > L[i]:
                    L[i] = 1 + L[j]
                    pre[i] = j
            if L[i] > maxL:
                maxL = L[i]
                maxpre = i
        result = [nums[maxpre]]
        while pre[maxpre] != maxpre:
            result.insert(0, nums[pre[maxpre]])
            maxpre = pre[maxpre]
        return result