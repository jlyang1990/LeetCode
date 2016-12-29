class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # two pointers
        sList = list(s)
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        left, right = 0, len(sList)-1
        while left < right:
            while left < right and sList[left] not in vowels:
                left += 1
            while left < right and sList[right] not in vowels:
                right -= 1
            if left < right:
                sList[left], sList[right] = sList[right], sList[left]
                left += 1
                right -= 1
        return "".join(sList)