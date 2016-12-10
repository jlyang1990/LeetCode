class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(candidates, target, 0, result, [])
        return result
        
    def dfs(self, candidates, target, start, result, combination):
        if target == 0:
            result.append(combination)
        elif target > 0:
            for i in range(start, len(candidates)):
                self.dfs(candidates, target-candidates[i], i, result, combination+[candidates[i]])