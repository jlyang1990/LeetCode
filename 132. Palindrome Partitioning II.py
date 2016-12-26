class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dynamic programming
        # palindrome[i][j]: whether s[i:j+1] is a palindrome
        # result[i]: minimum cuts needed for a palindrome partition of s[:i]
        # O(n^2) time, O(n^2) space (can be reduced to O(n)) space
        n = len(s)
        palindrome = [[True]*n for i in range(n)]
        result = [-1] + [float("inf")]*n
        for i in range(n):
            for j in range(i+1):
                palindrome[j][i] = (s[j] == s[i] and (i-j <= 2 or palindrome[j+1][i-1]))
                if palindrome[j][i]:
                    result[i+1] = min(result[i+1], result[j]+1)
        print result
        return result[n]