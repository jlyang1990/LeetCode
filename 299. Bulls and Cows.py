class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        # O(n) time (one-pass), O(1) space
        bull, cow = 0, 0
        count = [0]*10
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                if count[int(secret[i])] < 0:
                    cow += 1
                if count[int(guess[i])] > 0:
                    cow += 1
                count[int(secret[i])] += 1
                count[int(guess[i])] -= 1
        return str(bull)+"A"+str(cow)+"B"