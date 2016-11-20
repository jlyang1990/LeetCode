class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # when find a number nums[i], flip the number at position nums[i]-1 to negative and keep until the end
        # if the number at position j is positive, j+1 is the number disappeared
        for i in range(len(nums)):
            val = abs(nums[i]) - 1
            if nums[val] > 0:
                nums[val] = -nums[val]
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i+1)
        return result