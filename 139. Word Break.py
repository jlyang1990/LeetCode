class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
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
        return result[len(s)-1]