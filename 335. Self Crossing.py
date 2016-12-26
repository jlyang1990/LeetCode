class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        # O(n) time, O(1) space
        if len(x) <= 3:
            return False
        for i in range(3, len(x)):
            # Fourth line crosses first line and onward
            if x[i] >= x[i-2] and x[i-1] <= x[i-3]:
                return True
            if i >= 4:
                # Fifth line meets first line and onward
                if x[i]+x[i-4] >= x[i-2] and x[i-1] == x[i-3]:
                    return True
            if i >= 5:
                # Sixth line crosses first line and onward
                if x[i]+x[i-4] >= x[i-2] and x[i-1] <= x[i-3] and x[i-1]+x[i-5] >= x[i-3] and x[i-2] >= x[i-4]:
                    return True
        return False