class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        s.reverse()
        pre = 0
        for i in range(len(s)):
            if s[i] == " ":
                s[pre:i] = reversed(s[pre:i])
                pre = i+1
        s[pre:] = reversed(s[pre:])