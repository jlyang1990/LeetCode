class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        # O(len(nums)+logn) time
        missing, count, i = 1, 0, 0
        while missing <= n:
            if i < len(nums) and nums[i] <= missing:
                missing += nums[i]
                i += 1
            else:
                missing *= 2  # add "missing" into nums
                count += 1
        return count