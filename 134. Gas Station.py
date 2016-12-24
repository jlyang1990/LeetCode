class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # O(n) time, O(1) space
        # if [1 - n] < 0, no solution
        # if [1 - n] > 0, wlog, [1 - m] < 0, [m+1 - l] < 0, [l+1 - n] > 0
        # for 1<=i<m, [1 - i] > 0 => [l+1 - n] + [1 - i] > 0
        # for i = m, [m+1 - l] < 0 & [1 - n] > 0 => [l+1 - n] + [1 - m] > 0
        # for m+1<=i<l, [m+1 - i] > 0 => [l+1 - n] + [1 - m] + [m+1 - i] > 0
        # for i = l, [l+1 - n] + [1 - m] + [m+1 - l] = [1 - n] > 0
        current = 0
        for i in range(len(gas)):
            current += gas[i]-cost[i]
        if current < 0:
            return -1
        current = 0
        index = 0
        for i in range(len(gas)):
            current += gas[i]-cost[i]
            if current < 0:
                current = 0
                index = i+1
        return index