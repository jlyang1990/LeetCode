class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # one pass, two pointer
        left = 0
        right = len(nums)-1
        pointer = 0
        while pointer <= right:
            if nums[pointer] == 0:
                nums[left], nums[pointer] = nums[pointer], nums[left]
                left += 1
                pointer += 1
            elif nums[pointer] == 1:
                pointer += 1
            elif nums[pointer] == 2:
                nums[right], nums[pointer] = nums[pointer], nums[right]
                right -= 1  # no "pointer += 1" because nums[pointer] should be further investigated