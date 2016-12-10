class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates = sorted(candidates)
        self.dfs(candidates, target, 0, result, [])
        return result
        
    def dfs(self, candidates, target, start, result, combination):
        if target == 0:
            result.append(combination)
        elif target > 0:
            for i in range(start, len(candidates)):
                if i != start and candidates[i] == candidates[i-1]:
                    continue
                self.dfs(candidates, target-candidates[i], i+1, result, combination+[candidates[i]])