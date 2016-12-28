class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        oddCount = []
        for i in dic:
            if dic[i] %2 == 1:
                oddCount.append(i)
        if len(oddCount) > 1:
            return []
        result = []
        if len(oddCount) == 0:
            self.dfs(dic, result, "")
        if len(oddCount) == 1:
            self.dfs(dic, result, oddCount[0])
        return result
            
    
    def dfs(self, dic, result, pal):
        done = True
        for i in dic:
            if dic[i] >= 2:
                done = False
                dic[i] -= 2
                self.dfs(dic, result, i+pal+i)
                dic[i] += 2
        if done:
            result.append(pal)