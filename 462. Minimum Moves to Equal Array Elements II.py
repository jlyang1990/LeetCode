class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        median = self.quickSelect(nums, 0, len(nums)-1, len(nums)/2)
        return sum([abs(n-median) for n in nums])
        
    def quickSelectHelper(self, nums, start, end):
        # pick the middle point in nums[start:end+1] as pivot
        # try to avoid the slow cases in quick select
        nums[start], nums[(start+end)/2] = nums[(start+end)/2], nums[start]
        pivot = nums[start]
        left = start+1
        right = end
        while left <= right:
            while left <= right and nums[left] <= pivot:
                left += 1
            while left <= right and nums[right] >= pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
        nums[start], nums[right] = nums[right], nums[start]
        return right
        
    def quickSelect(self, nums, start, end, k):
        pos = self.quickSelectHelper(nums, start, end)
        if pos == k:
            return nums[pos]
        elif pos > k:
            return self.quickSelect(nums, start, pos-1, k)
        else:
            return self.quickSelect(nums, pos+1, end, k)