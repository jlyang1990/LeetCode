class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.decodeStringHelper(s, 0)[0]
        
        
    def decodeStringHelper(self, s, i):
        result = ""
        while i < len(s) and s[i] != "]":
            if not s[i].isdigit():  # s[i] is character
                result += s[i]
                i += 1
            else:
                n = 0
                while s[i].isdigit():
                    n = n*10 + int(s[i])
                    i += 1
                i += 1  # surpass inner "["
                temp_result, temp_i = self.decodeStringHelper(s, i)
                for j in range(n):
                    result += temp_result
                i = temp_i+1  # surpass inner "]"
        return result, i  # i: index of (outer) "]"