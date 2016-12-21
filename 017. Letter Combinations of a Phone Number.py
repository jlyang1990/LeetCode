class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        charmap = [" ", "*", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        result = []
        self.dfs(digits, 0, charmap, result, "")
        return result
        
        
    def dfs(self, digits, start, charmap, result, char):
        if start == len(digits):
            result.append(char)
        else:
            for s in charmap[int(digits[start])]:
                self.dfs(digits, start+1, charmap, result, char+s)