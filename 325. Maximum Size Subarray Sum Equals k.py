class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # O(n) time, O(n) space 
        cumSum = 0
        cumSums = {0:0}  # store the smallest index of given cumSum
        maxLen = 0
        for i in range(len(nums)):
            cumSum += nums[i]
            if cumSum-k in cumSums:
                maxLen = max(maxLen, i+1-cumSums[cumSum-k])
            if cumSum not in cumSums:  # if cumSum in cumSums, should not update since we need the smallest index of cumSum
                cumSums[cumSum] = i+1
        return maxLen