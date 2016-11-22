class Solution(object):
    def permuteUnique(self, nums):
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
                    # think about creating [1,2,1,2,1,2] by add 2
                    # there are three cases: [1,_,1,2,1,2], [1,2,1,_,1,2], [1,2,1,2,1,_] yield the same result
                    # only keep the case where 2 is added as the first 2, i.e., stop adding 2 when we meet 2
                    if insert_loc < insert_index and nums[insert_index] == element[insert_loc]:
                        break
            result = temp
        return result