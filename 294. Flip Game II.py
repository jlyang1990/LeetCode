class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        winDic = {}
        return self.canWinHelper(s, winDic)
        
        
    def canWinHelper(self, s, winDic):
        if s in winDic:
            return winDic[s]
        for i in range(len(s)-1):
            if s[i:i+2] == "++" and not self.canWinHelper(s[:i]+"--"+s[i+2:], winDic):
                winDic[s] = True
                return True
        winDic[s] = False
        return False