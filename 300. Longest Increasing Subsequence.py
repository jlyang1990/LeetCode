class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # "tails" is an array containing the smallest tail of all increasing subsequences with length i+1 in tails[i]
        # "tails" is an increasing array. It is possible to do a binary search in "tails" to find the one needs update
        # Each time we only do one of the two:
        # 1. if x is larger than all tails, append it, increase the size by 1
        # 2. if tails[i-1] < x <= tails[i], update tails[i]
        # O(nlogn) time, O(n) space
        
        # method 1
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) / 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size
        

        # method 2
        tails = [0]*len(nums)
        size = 0
        for x in nums:
            left, right = 0, size-1
            while left <= right:
                mid = (left+right)//2
                if tails[mid] < x:
                    left = mid+1
                else:
                    right = mid-1
            tails[left] = x
            size = max(size, left+1)
        return size