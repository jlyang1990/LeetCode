class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        result = ""
        for i in range(numRows):
            for j in range(i, len(s), (numRows-1)*2):
                result += s[j]
                if j+(numRows-1)*2-2*i < len(s) and i != 0 and i != numRows-1:
                    result += s[j+(numRows-1)*2-2*i]
        return result