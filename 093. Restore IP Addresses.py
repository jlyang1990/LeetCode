class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) > 12:
            return []
        result = []
        self.dfs(s, 0, 4, result, "")
        return result
        
        
    def dfs(self, s, start, k, result, address):
        if start == len(s) and k == 0:
            result.append(address[1:])
        elif start == len(s) or k == 0:
            return
        else:
            self.dfs(s, start+1, k-1, result, address+"."+s[start])
            if s[start] != "0" and start < len(s)-1:
                self.dfs(s, start+2, k-1, result, address+"."+s[start:start+2])
            if s[start] != "0" and start < len(s)-2 and int(s[start:start+3]) < 256:
                self.dfs(s, start+3, k-1, result, address+"."+s[start:start+3])