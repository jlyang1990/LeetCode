class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        loc = 0
        for i in nums:
            if i != 0:
                nums[loc] = i
                loc += 1
        for j in range(loc, len(nums)):
            nums[j] = 0