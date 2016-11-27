class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dynamic programming: f(k) = max(f(k-1), f(k-2)+nums[k])
        current, previous = 0, 0
        for i in nums:
            current, previous = max(current, previous+i), current
        return current