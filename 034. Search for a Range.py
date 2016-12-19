class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # find smallest index that nums[index] >= target (index = len(nums) means no index)
        # O(logn) time
        left, right = 0, len(nums)
        while left < right:
            mid = (left+right)/2  # bias to smaller index so that "right = mid" can always move
            if nums[mid] < target:
                left = mid+1
            else:
                right = mid
        left_target = left
        # find largest index that nums[index] <= target (index = -1 means no index)
        # O(logn) time
        left, right = -1, len(nums)-1
        while left < right:
            mid = (left+right+1)/2  # bias to larger index so that "left = mid" can always move
            if nums[mid] > target:
                right = mid-1
            else:
                left = mid
        right_target = left
        return [left_target, right_target] if left_target <= right_target else [-1, -1]