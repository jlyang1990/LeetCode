class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # length[i]: longest length of valid parentheses ending at i
        # length[i] = 0, if s[i] = "("
        # length[i] = length[i-2] + 2, if s[i] = ")" and s[i-1] = "("
        # length[i] = length[i-1] + 2 + length[i-length[i-1]-2], if s[i] = ")" and s[i-1] = ")" and s[i-length[i-1]-1] = "("
        # length[i] = 0, if s[i] = ")" and s[i-1] = ")" and (i-length[i-1]-1 < 0 or s[i-length[i-1]-1] = ")")
        # O(n) time, O(n) space
        length = [0]*len(s)
        maxLength = 0
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i-1] == "(":
                    length[i] = 2 + (length[i-2] if i-2 >= 0 else 0)
                    maxLength = max(maxLength, length[i])
                else:
                    if i-length[i-1]-1 >= 0 and s[i-length[i-1]-1] == "(":
                        length[i] = length[i-1] + 2 + (length[i-length[i-1]-2] if i-length[i-1]-2 >= 0 else 0)
                        maxLength = max(maxLength, length[i])
        return maxLength