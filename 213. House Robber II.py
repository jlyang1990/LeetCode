class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # house 0 and house n-1 cannot be both robbed
        # either house 0 is not robbed or house n-1 is not robbed
        if len(nums) == 1:
            return nums[0]
        return max(self.robHelper(nums[1:]), self.robHelper(nums[:-1]))
        
    def robHelper(self, nums):
        current, previous = 0, 0
        for i in nums:
            current, previous = max(current, previous+i), current
        return current