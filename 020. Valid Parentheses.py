class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {}
        dic["("] = ")"
        dic["{"] = "}"
        dic["["] = "]"
        stack = []
        for current in s:
            if current in dic:
                stack.append(current)
            else:
                if len(stack) == 0:
                    return False
                previous = stack.pop()
                if dic[previous] != current:
                    return False
        return len(stack) == 0