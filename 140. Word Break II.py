class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        # Word Break I
        # O(n^2) time, O(n) space
        result = [False]*len(s)
        for i in range(len(s)):
            if s[:i+1] in wordDict:
                result[i] = True
                continue
            for j in range(i):
                if result[j] and s[j+1:i+1] in wordDict:
                    result[i] = True
                    break
        if not result[len(s)-1]:
            return []
        
        # method 1: dynamic programming
        results = [[] for i in range(len(s))]
        for i in range(len(s)):
            if s[:i+1] in wordDict:
                results[i].append(s[:i+1])
            for j in range(i):
                if results[j] and s[j+1:i+1] in wordDict:
                    for result in results[j]:
                        results[i].append(result + " " + s[j+1:i+1])
        return results[len(s)-1]

        
        # method 2: dfs
        lenDict = set()
        for word in wordDict:
            lenDict.add(len(word))
        result = []
        self.dfs(s, wordDict, lenDict, 0, result, "")
        return result
        
        
    def dfs(self, s, wordDict, lenDict, start, result, char):
        if start == len(s):
            result.append(char[:len(char)-1])
        else:
            for i in lenDict:
                if start + i <= len(s) and s[start:start+i] in wordDict:
                    self.dfs(s, wordDict, lenDict, start+i, result, char + s[start:start+i] + " ")