class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count = [0]*26
        for s in magazine:
            count[ord(s)-ord("a")] += 1
        for s in ransomNote:
            count[ord(s)-ord("a")] -= 1
            if count[ord(s)-ord("a")] < 0:
                return False
        return True