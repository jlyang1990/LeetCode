class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # put numbers 1-n into their right places
        # O(n) time, O(1) space
        n = len(nums)
        for i in range(n):
            while nums[i] > 0 and nums[i] <= n and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i]  = nums[i], nums[nums[i]-1]
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1