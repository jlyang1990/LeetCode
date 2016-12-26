class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # O(nk^2) time, where k is the average length of words
        dic = {}
        result = set()  # use set to remove duplicated combinations
        for i in range(len(words)):
            dic[words[i][::-1]] = i
        for i in range(len(words)):
            # use range(len(words[i])+1) instead of range(len(words[i])) to allow consideration of "" in words
            for j in range(len(words[i])+1):
                leftWord = words[i][:j]
                rightWord = words[i][j:]
                if leftWord in dic and dic[leftWord] != i and self.isPalindrome(rightWord):
                    result.add((i, dic[leftWord]))
                if rightWord in dic and dic[rightWord] != i and self.isPalindrome(leftWord):
                    result.add((dic[rightWord], i))
        return [list(x) for x in result]
        
    def isPalindrome(self, word):
        left, right = 0, len(word)-1
        while left < right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True