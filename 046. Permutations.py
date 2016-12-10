class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # method 1
        result = [[]]
        for insert_index in range(len(nums)):
            temp = []
            for element in result:
                for insert_loc in range(insert_index+1):
                    temp.append(element[:insert_loc] + [nums[insert_index]] + element[insert_loc:])
            result = temp
        return result

        # method 2: dfs
        result = []
        self.dfs(nums, result, [])
        return result
    
    def dfs(self, nums, result, permutation):
        if len(nums) == 0:
            result.append(permutation)
        else:
            for i in range(len(nums)):
                self.dfs(nums[:i]+nums[i+1:], result, permutation+[nums[i]])