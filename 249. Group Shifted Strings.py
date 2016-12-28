class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        stringDic = {}
        for string in strings:
            stringShift = self.shift(string)
            if stringShift not in stringDic:
                stringDic[stringShift] = [string]
            else:
                stringDic[stringShift].append(string)
        return [stringDic[stringShift] for stringShift in stringDic]
        
        
    def shift(self, string):
        start = string[0]
        return tuple([ord(x)-ord(start) if ord(x)-ord(start) >= 0 else ord(x)-ord(start)+26 for x in string])