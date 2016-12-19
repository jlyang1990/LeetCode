class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # O(n) time, O(1) space
        counts = [0]*26
        start = 0
        maxCount = 0
        maxLength = 0
        for end in range(len(s)):
            counts[ord(s[end])-ord("A")] += 1
            maxCount = max(maxCount, counts[ord(s[end])-ord("A")])
            while end-start+1-maxCount > k:
                counts[ord(s[start])-ord("A")] -= 1
                start += 1
                maxCount = max(counts)
            maxLength = max(maxLength, end-start+1)
        return maxLength