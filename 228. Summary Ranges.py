class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # two pointer
        result = []
        i = 0
        while i < len(nums):
            j = i+1
            while j < len(nums) and nums[j] - nums[j-1] == 1:
                j += 1
            if nums[j-1] == nums[i]:
                result.append(str(nums[i]))
            else:
                result.append(str(nums[i]) + "->" + str(nums[j-1]))
            i = j
        return result