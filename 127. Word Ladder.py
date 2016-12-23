class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        if beginWord in wordList:
            wordList.remove(beginWord)
        wordList.add(endWord)
        wordQueue = []
        self.addNextWords(beginWord, wordList, wordQueue)
        dist = 2
        while wordQueue:
            tempQueue = []
            while wordQueue:
                word = wordQueue.pop()
                if word == endWord:
                    return dist
                self.addNextWords(word, wordList, tempQueue)
            wordQueue = tempQueue
            dist += 1
        return 0
        
        
    def addNextWords(self, beginWord, wordList, wordQueue):
        for i in range(len(beginWord)):
            for j in range(26):
                newWord = beginWord[:i]+(chr(ord("a")+j))+beginWord[i+1:]
                if newWord in wordList:
                    wordQueue.append(newWord)
                    wordList.remove(newWord)