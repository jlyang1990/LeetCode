class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m, n = len(haystack), len(needle)
        for i in range(m-n+1):
            find = True
            for j in range(n):
                if haystack[i+j] != needle[j]:
                    find = False
                    break
            if find:
                return i
        return -1