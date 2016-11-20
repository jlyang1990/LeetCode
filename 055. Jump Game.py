class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # O(n) time complexity
        reach = 0
        i = 0
        while i <= reach and reach < len(nums)-1:
            reach = max(i+nums[i], reach)
            i += 1
        return reach >= len(nums)-1