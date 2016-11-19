class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dynamic programming
        # maxSubArray = max(maxSubArray(endwithindex0), maxSubArray(endwithindex1), ..., maxSubArray(endwithindex(n-1)))
        maxsum = [None] * len(nums)
        maxsum[0] = nums[0]
        for i in range(1, len(nums)):
            maxsum[i] = max(maxsum[i-1], 0) + nums[i]
        return max(maxsum)