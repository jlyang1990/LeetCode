class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # method 1
        result = [[]]
        for insert_num in nums:
            temp = []
            for element in result:
                temp.append(element)
                temp.append(element+[insert_num])  
                # element+[insert_num] is a new variable, thus element is not changed
                # if use element.append(insert_num), element is changed (side effect)!
            result = temp
        return result
        
        # method 2: dfs
        result = []
        self.dfs(nums, 0, result, [])
        return result
        
    def dfs(self, nums, start, result, subset):
        if start == len(nums):
            result.append(subset)
        else:
            self.dfs(nums, start+1, result, subset)
            self.dfs(nums, start+1, result, subset+[nums[start]])