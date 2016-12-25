class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n) time
        dic = {}
        maxLen = 0
        for num in nums:
            if num not in dic:
                left = dic[num-1] if num-1 in dic else 0
                right = dic[num+1] if num+1 in dic else 0
                length = left+right+1
                dic[num] = length
                dic[num-left] = length  # update two end points is enough
                dic[num+right] = length  # update two end points is enough
                maxLen = max(maxLen, length)
        return maxLen