class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for insert_index in range(len(nums)):
            temp = []
            for element in result:
                for insert_loc in range(insert_index+1):
                    temp.append(element[:insert_loc] + [nums[insert_index]] + element[insert_loc:])
            result = temp
        return result