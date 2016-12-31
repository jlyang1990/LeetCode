class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # moving window
        # O(n) time
        result = ""
        dic = {}
        for i in t:
            if i not in dic:
                dic[i] = -1
            else:
                dic[i] += -1
        left, right = 0, 0
        minLen = float("inf")
        count = 0
        while right < len(s):
            while right < len(s) and count < len(t):
                if s[right] in dic:
                    dic[s[right]] += 1
                    if dic[s[right]] <= 0:
                        count += 1
                right += 1
            if count == len(t):
                while s[left] not in dic or dic[s[left]] > 0:
                    if s[left] in dic:
                        dic[s[left]] -= 1
                    left += 1
                if right - left < minLen:
                    minLen = right - left
                    result = s[left:right]
                dic[s[left]] -= 1
                count -= 1
                left += 1
        return result