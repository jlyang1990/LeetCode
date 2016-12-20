class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # O(n) time, O(n) space
        if t < 0:
            return False
        dic = {}
        for i in range(len(nums)):
            pos = nums[i]/(t+1)
            if pos in dic or (pos+1 in dic and dic[pos+1]-nums[i] <= t) or (pos-1 in dic and nums[i]-dic[pos-1] <= t):
                return True
            dic[pos] = nums[i]
            if i >= k:
                del dic[nums[i-k]/(t+1)]
        return False