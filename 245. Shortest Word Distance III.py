class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # O(n) time
        minDist = float("inf")
        if word1 != word2:
            word1Pos, word2Pos = float("inf"), float("inf")
            for i in range(len(words)):
                if words[i] == word1:
                    word1Pos = i
                if words[i] == word2:
                    word2Pos = i
                minDist = min(minDist, abs(word1Pos - word2Pos))
        else:
            wordPos = float("-inf")
            minDist = float("inf")
            for i in range(len(words)):
                if words[i] == word1:
                    minDist = min(minDist, i - wordPos)
                    wordPos = i
            return minDist