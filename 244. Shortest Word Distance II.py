class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        # O(n) time
        self.wordsDic = {}
        for i in range(len(words)):
            if words[i] not in self.wordsDic:
                self.wordsDic[words[i]] = [i]
            else:
                self.wordsDic[words[i]].append(i)
        

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # O(l1+l2) time, li is the total number of positions of wordi
        pos1, pos2 = self.wordsDic[word1], self.wordsDic[word2]
        i, j = 0, 0
        minDist = float("inf")
        while i < len(pos1) and j < len(pos2):
            if pos1[i] <= pos2[j]:
                minDist = min(minDist, pos2[j]-pos1[i])
                i += 1
            else:
                minDist = min(minDist, pos1[i]-pos2[j])
                j += 1
        return minDist
        


# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")