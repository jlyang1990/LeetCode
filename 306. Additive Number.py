class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        for i in range(1, n-1):
            for j in range(i+1, n):
                a, b = num[:i], num[i:j]
                if a != str(int(a)) or b != str(int(b)):
                    continue
                match = True
                while j < n:
                    c = str(int(a) + int(b))
                    for k in range(len(c)):
                        if j+k == n or num[j+k] != c[k]:
                            match = False
                            break
                    if match == False:
                        break
                    j += len(c)
                    a, b = b, c
                if j == n:
                    return True
        return False