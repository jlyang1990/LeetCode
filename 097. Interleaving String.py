class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # result[i, j]: whether s3[:i+j] is formed by the interleaving of s1[:i] and s2[:j]
        # result[i, j] = result[i-1, j] or result[i, j-1] if s3[i+j-1] = s1[i-1] = s2[j-1]
        # result[i, j] = result[i-1, j] if s3[i+j-1] = s1[i-1]
        # result[i, j] = result[i, j-1] if s3[i+j-1] = s2[j-1]
        # result[0, 0] = True
        # O(mn) time, O(min(m, n)) space
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        result = [True]+[False]*n
        for j in range(1, n+1):
            result[j] = result[j-1] and s3[j-1] == s2[j-1]
        for i in range(1, m+1):
            result[0] = result[0] and s3[i-1] == s1[i-1]
            for j in range(1, n+1):
                result[j] = (result[j-1] and s3[i+j-1] == s2[j-1]) or (result[j] and s3[i+j-1] == s1[i-1])
        return result[n]