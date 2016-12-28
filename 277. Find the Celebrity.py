# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0
        for i in range(1, n):
            # if knows(i, candidate), i cannot be celebrity
            # if not knows(i, candidate), candidate cannot be celebrity
            if not knows(i, candidate):
                candidate = i
        # check whether candidate is celebrity
        for i in range(n):
            # (i > candidate and knows(i, candidate)) has already been proved true
            if (i != candidate and knows(candidate, i)) or (i < candidate and not knows(i, candidate)):
                return -1
        return candidate