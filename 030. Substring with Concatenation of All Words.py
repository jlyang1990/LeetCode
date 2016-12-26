class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result = []
        n, m = len(s), len(words)
        if n == 0 or m == 0:
            return result
        l = len(words[0])
        dic = {}
        for word in words:
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] += 1
        
        # travel all possible starting point to set "left"        
        for i in range(l):
            left = i
            count = 0
            tempDic = {}
            for j in range(i, n-l+1, l):
                word = s[j:j+l]
                if word in dic:
                    # valid word
                    if word not in tempDic:
                        tempDic[word] = 1
                    else:
                        tempDic[word] += 1
                    count += 1
                    # redundant "word", advance "left"
                    while tempDic[word] > dic[word]:
                        tempDic[s[left:left+l]] -= 1
                        count -= 1
                        left += l
                    # find a solution, advance "left"
                    if count == m:
                        result.append(left)
                        tempDic[s[left:left+l]] -= 1
                        count -= 1
                        left += l
                else:
                    # invalid word, start over
                    left = j+l
                    count = 0
                    tempDic = {}
        return result