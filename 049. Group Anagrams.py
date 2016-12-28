class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        dic = {}
        for word in strs:
            char = tuple(sorted(list(word)))
            if char not in dic:
                dic[char] = [word]
            else:
                dic[char].append(word)
        for char in dic:
            result.append(dic[char])
        return result