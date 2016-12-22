class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left, right, subsum, minlen = 0, 0, 0, float("inf")
        while right < len(nums):
            while right < len(nums) and subsum < s:
                right += 1
                subsum += nums[right-1]
            if subsum < s:
                break
            while subsum >= s:
                subsum -= nums[left]
                left += 1
            minlen = min(minlen, right-left+1)
        return minlen if minlen < float("inf") else 0