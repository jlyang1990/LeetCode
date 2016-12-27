class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # dfs
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        nums_dic = [(j, dic[j]) for j in dic]
        result = []
        self.dfs(nums_dic, 0, result, [])
        return result
        
    def dfs(self, nums_dic, start, result, subset):
        if start == len(nums_dic):
            result.append(subset)
        else:
            for i in range(nums_dic[start][1]+1):
                self.dfs(nums_dic, start+1, result, subset+[nums_dic[start][0]]*i)