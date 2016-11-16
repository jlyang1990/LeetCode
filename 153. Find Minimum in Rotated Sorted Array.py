class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # binary search
        first = 0
        last = len(nums) - 1
        while first < last:
            mid = (first+last)/2
            if nums[mid] < nums[last]:
                last = mid
            else:
                first = mid + 1
        return nums[first]