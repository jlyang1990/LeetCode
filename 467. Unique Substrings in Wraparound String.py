class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        # maxlen[i]: maximum length substring ending with ith letter
        # O(n) time, O(1) space
        maxlen = [0]*26
        for i in range(len(p)):
            if i > 0 and (ord(p[i])-ord(p[i-1]) == 1 or ord(p[i])-ord(p[i-1]) == -25):
                curlen += 1
            else:
                curlen = 1
            maxlen[ord(p[i])-ord("a")] = max(maxlen[ord(p[i])-ord("a")], curlen)
        return sum(maxlen)