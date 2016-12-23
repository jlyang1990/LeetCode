class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # O(n) time
        dic = {}
        freq = [[] for i in s]
        result = ""
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for i in dic:
            freq[dic[i]-1].append(i)
        for i in range(len(freq)-1, -1, -1):
            while freq[i]:
                char = freq[i].pop()
                result += char*(i+1)
        return result