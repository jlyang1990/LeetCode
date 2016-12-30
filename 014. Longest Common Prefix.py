class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        strs.sort(key = lambda x: len(x))
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i][:len(prefix)] != prefix:
                prefix = prefix[:len(prefix)-1]
        return prefix