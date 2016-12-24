class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # dynamic programming
        # palindrome[i][j]: whether s[i:j+1] is a palindrome
        # result[i]: palindrome partitions of s[:i]
        n = len(s)
        palindrome = [[True]*n for i in range(n)]
        result = [[[]]] + [[] for i in range(n)]
        for i in range(n):
            for j in range(i+1):
                palindrome[j][i] = (s[j] == s[i] and (i-j <= 2 or palindrome[j+1][i-1]))
                if palindrome[j][i]:
                    for partition in result[j]:
                        result[i+1].append(partition+[s[j:i+1]])
        return result[n]