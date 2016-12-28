class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        result = []
        self.dfs(word, 0, result, "")
        return result
        
        
    def dfs(self, word, start, result, abbr):
        if start == len(word):
            result.append(abbr)
        else:
            self.dfs(word, start+1, result, abbr+word[start])
            for i in range(1, len(word)-start+1):
                if start == 0 or not abbr[-1].isdigit():
                    self.dfs(word, start+i, result, abbr+str(i))