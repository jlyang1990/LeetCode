class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dic[x] = largest index of x so far
        # O(n) time, O(n) space
        dic = {}
        start = 0
        longest = 0
        for i in range(len(s)):
            if s[i] in dic:
                start = max(start, dic[s[i]]+1)
            dic[s[i]] = i
            longest = max(longest, i-start+1)
        return longest