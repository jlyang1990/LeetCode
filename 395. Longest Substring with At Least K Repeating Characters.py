class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        return self.longestSubstringHelper(s, k, 0, len(s)-1)
        
    # divide and conquer
    # O(nlogn) time
    def longestSubstringHelper(self, s, k, start, end):
        if end-start+1 < k or end < start:
            return 0
        counts = [0]*26
        for i in range(start, end+1):
            counts[ord(s[i])-ord("a")] += 1
        for i in range(start, end+1):
            if counts[ord(s[i])-ord("a")] < k and counts[ord(s[i])-ord("a")] > 0:
                left_len = self.longestSubstringHelper(s, k, start, i-1)
                right_len = self.longestSubstringHelper(s, k, i+1, end)
                return max(left_len, right_len)
        return end-start+1