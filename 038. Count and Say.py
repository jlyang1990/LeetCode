class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        for i in range(n-1):
            result = self.nextCount(s)
            s = result
        return s
        
    def nextCount(self, s):
        result = ""
        count = 0
        for i in range(len(s)):
            count += 1
            if i == len(s)-1 or s[i+1] != s[i]:
                result += str(count) + s[i]
                count = 0
        return result