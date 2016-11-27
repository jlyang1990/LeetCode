class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # quick selection
        # average time complexity: O(n)+O(n/2)+O(n/4)+...=O(n)
        def partition(nums, first, last):
            left = first+1
            right = last
            while left <= right:
                while left <= right and nums[left] <= nums[first]:
                    left += 1
                while left <= right and nums[right] >= nums[first]:
                    right -= 1
                if left <= right:
                    nums[left], nums[right] = nums[right], nums[left]
            nums[first], nums[right] = nums[right], nums[first]
            return right
            
        def findKthLargestHelper(nums, k, first, last):
            loc = partition(nums, first, last)
            if loc == len(nums) - k:
                return nums[loc]
            elif loc < len(nums) - k:
                return findKthLargestHelper(nums, k, loc+1, last)
            else:
                return findKthLargestHelper(nums, k, first, loc-1)
        
        return findKthLargestHelper(nums, k, 0, len(nums)-1)