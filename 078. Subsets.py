class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for insert_num in nums:
            temp = []
            for element in result:
                temp.append(element[:])
                element.append(insert_num)
                temp.append(element)
            result = temp
        return result