class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # count[i][j]: number of distinct subsequences of t[:i] in s[:j]
        # count[0][j] = 1
        # count[i][0] = 0, i != 0
        # count[i][j] = count[i][j-1] if t[i-1] != s[j-1]
        # count[i][j] = count[i][j-1]+count[i-1][j-1] if t[i-1] = s[j-1]
        # O(mn) time, O(m) space
        m, n = len(t), len(s)
        count = [1]+[0]*m  # first column of count matrix
        for j in range(n):
            pre = 1
            for i in range(m):
                temp = count[i+1]
                if t[i] == s[j]:
                    count[i+1] += pre
                pre = temp
        return count[m]