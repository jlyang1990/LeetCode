class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        add = 1
        while digits:
            val = digits.pop() + add
            if val >= 10:
                result.append(val%10)
                add = 1
            else:
                result.append(val)
                add = 0
        if add:
            result.append(1)
        return result[::-1]