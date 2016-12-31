class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # O(n*26) = O(n) time
        if len(s) == 0:
            return s
        count = [0]*26
        for i in range(len(s)):
            count[ord(s[i])-ord("a")] += 1
        pos = 0
        for i in range(len(s)):
            if s[i] < s[pos]:  # find pos with the smallest s[pos]
                pos = i
            count[ord(s[i])-ord("a")] -= 1
            if count[ord(s[i])-ord("a")] == 0:  # the right side of pos (inclusive) should contain all the distinct letters in s
                break
        return s[pos]+self.removeDuplicateLetters(s[pos+1:].replace(s[pos], ""))