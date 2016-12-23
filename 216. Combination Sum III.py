class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(k, n, 1, result, [])
        return result
        
        
    def dfs(self, k, n, start, result, nums):
        if k == 0 and n == 0:
            result.append(nums)
        elif k == 0 or n == 0:
            return
        else:
            for i in range(start, min(n+1, 10)):
                self.dfs(k-1, n-i, i+1, result, nums+[i])