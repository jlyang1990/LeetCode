class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        # O(n+k) time
        result = [0]*(length+1)
        for update in updates:
            result[update[0]] += update[2]  # set the start flag of cummulative sum
            result[update[1]+1] -= update[2]  # set the end flag of cummulative sum
        for i in range(1, length):
            result[i] += result[i-1]
        return result[:length]