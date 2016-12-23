class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        # bfs in finding shortest distance
        # dfs in outputing paths
        if beginWord in wordList:
            wordList.remove(beginWord)
        wordList.add(endWord)
        wordQueue = set()
        wordDict = {}
        self.addNextWords(beginWord, wordList, wordQueue, wordDict)
        for word in wordQueue:
            wordList.remove(word)
        result = []
        while wordQueue:
            tempQueue = set()
            while wordQueue:
                word = wordQueue.pop()
                if word == endWord:
                    self.outputPaths(endWord, beginWord, wordDict, result, [])
                    return result
                self.addNextWords(word, wordList, tempQueue, wordDict)
            for word in tempQueue:
                wordList.remove(word)
            wordQueue = tempQueue
        return result
        
        
    def addNextWords(self, beginWord, wordList, wordQueue, wordDict):
        for i in range(len(beginWord)):
            for j in range(26):
                newWord = beginWord[:i]+(chr(ord("a")+j))+beginWord[i+1:]
                if newWord in wordList:
                    wordQueue.add(newWord)
                    if newWord not in wordDict:
                        wordDict[newWord] = [beginWord]
                    else:
                        wordDict[newWord].append(beginWord)
                        
    
    def outputPaths(self, curWord, beginWord, wordDict, result, path):
        if curWord == beginWord:
            path = [curWord]+path 
            result.append(path)
        else:
            for word in wordDict[curWord]:
                self.outputPaths(word, beginWord, wordDict, result, [curWord]+path)