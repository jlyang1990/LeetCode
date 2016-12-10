class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # dynamic programming
        # O(sum(nums)*n) time, O(sum(nums)) space
        if sum(nums) % 2 == 1:
            return False
        s = sum(nums) / 2
        sum_array = [True] + [False] * s
        for num in nums:
            for i in range(s - num, -1, -1):
                if sum_array[i] == True:
                    sum_array[i + num] = True
        return sum_array[s]