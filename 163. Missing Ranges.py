class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if len(nums) == 0:
            return [str(lower) + "->" + str(upper)] if lower < upper else [str(lower)]
        result = []
        if nums[0] > lower:
            missingRange = str(lower) + "->" + str(nums[0]-1) if nums[0] > lower+1 else str(lower)
            result.append(missingRange)
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]+1:
                missingRange = str(nums[i-1]+1) + "->" + str(nums[i]-1) if nums[i] > nums[i-1]+2 else str(nums[i]-1)
                result.append(missingRange)
        if nums[-1] < upper:
            missingRange = str(nums[-1]+1) + "->" + str(upper) if upper > nums[-1]+1 else str(upper)
            result.append(missingRange)
        return result