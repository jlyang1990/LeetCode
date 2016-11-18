class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dynamic programming
        # maxProduct = max(maxProduct(endwithindex0), maxProduct(endwithindex1), ..., maxProduct(endwithindex(n-1)))
        n = len(nums)
        maxprod = [None]*n
        minprod = [None]*n
        maxprod[0] = nums[0]
        minprod[0] = nums[0]
        for i in range(1, len(nums)):
            maxprod[i] = max([nums[i], maxprod[i-1]*nums[i], minprod[i-1]*nums[i]])
            minprod[i] = min([nums[i], maxprod[i-1]*nums[i], minprod[i-1]*nums[i]])
        return max(maxprod)