class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = float("inf")  # smallest (valid) first element in triplet 
                              # or (potential) first element in triplet (for searching for better "second") up to i-1
        second = float("inf")  # smallest (valid) second element in triplet up to i-1
                               # nums[i] must be larger than "second" to complete a triplet
        for i in nums:
            if i < first:
                first = i
            if i > first and i < second:
                second = i
            if i > second:
                return True
        return False