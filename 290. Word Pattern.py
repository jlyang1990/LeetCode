class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # O(n) time, O(n) space
        word = str.split()
        if len(pattern) != len(word):
            return False
        patternDic = {}
        wordDic = {}
        for i in range(len(pattern)):
            if pattern[i] in patternDic and patternDic[pattern[i]] != word[i]:
                return False
            if pattern[i] not in patternDic:
                patternDic[pattern[i]] = word[i]
            if word[i] in wordDic and wordDic[word[i]] != pattern[i]:
                return False
            if word[i] not in wordDic:
                wordDic[word[i]] = pattern[i]
        return True