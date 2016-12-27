class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # O(n^2) time
        nums.sort()
        count = 0
        for first in range(len(nums)):
            left, right = first+1, len(nums)-1
            while left < right:
                if nums[left] + nums[right] < target-nums[first]:
                    count += right - left
                    left += 1
                else:
                    right -= 1
        return count