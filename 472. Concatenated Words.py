class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # O(len(word1)^2+...+len(wordn)^2) time
        if len(words) <= 2:
            return []
        words = sorted(words, key = lambda x: len(x))
        result = []
        wordDict = set()
        for word in words:
            if self.wordBreak(word, wordDict):
                result.append(word)
            wordDict.add(word)
        return result
        
        
    def wordBreak(self, word, wordDict):    
        result = [False]*len(word)
        for i in range(len(word)):
            if word[:i+1] in wordDict:
                result[i] = True
                continue
            for j in range(i):
                if result[j] and word[j+1:i+1] in wordDict:
                    result[i] = True
                    break
        return result[len(word)-1]