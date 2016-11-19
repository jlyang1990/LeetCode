class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        indicator = 0
        count = 1
        for i in range(len(nums)-1):
            if indicator == 0:
                if (nums[i+1] - nums[i]) > 0:
                    indicator = 1
                    count += 1
                if (nums[i+1] - nums[i]) < 0:
                    indicator = -1
                    count += 1
            else:
                if indicator * (nums[i+1] - nums[i]) < 0:
                    indicator = -indicator
                    count += 1
        return count