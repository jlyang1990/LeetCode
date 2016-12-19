class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        # Reservior Sampling
        # O(n) time, O(1) space
        from random import random
        index = -1
        count = 0
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                if random() <= 1.0/(1+count):
                    index = i
                count += 1
        return index
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)