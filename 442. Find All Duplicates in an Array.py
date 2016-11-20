class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # when find a number nums[i], flip the number at position nums[i]-1 to negative
        # if the number at position nums[i]-1 is already negative, nums[i] is the number that occurs twice
        result = []
        for i in range(len(nums)):
            val = abs(nums[i]) - 1
            if nums[val] > 0:
                nums[val] = -nums[val]
            else:
                result.append(val+1)
        return result