class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = [0]*26
        count = [0]*10
        result = ""
        for i in s:
            dic[ord(i)-ord("a")] += 1
        count[0] = dic[ord("z")-ord("a")]
        count[1] = dic[ord("o")-ord("a")]-dic[ord("z")-ord("a")]-dic[ord("w")-ord("a")]-dic[ord("u")-ord("a")]
        count[2] = dic[ord("w")-ord("a")]
        count[3] = dic[ord("h")-ord("a")]-dic[ord("g")-ord("a")]
        count[4] = dic[ord("u")-ord("a")]
        count[5] = dic[ord("f")-ord("a")]-dic[ord("u")-ord("a")]
        count[6] = dic[ord("x")-ord("a")]
        count[7] = dic[ord("s")-ord("a")]-dic[ord("x")-ord("a")]
        count[8] = dic[ord("g")-ord("a")]
        count[9] = dic[ord("i")-ord("a")]-dic[ord("x")-ord("a")]-dic[ord("g")-ord("a")]-dic[ord("f")-ord("a")]+dic[ord("u")-ord("a")]
        for i in range(10):
            result += str(i)*count[i]
        return result