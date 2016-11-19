class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """    
        loc = 0
        for i in nums:
            if i != val:
                nums[loc] = i
                loc += 1
        nums = nums[:loc]
        return loc