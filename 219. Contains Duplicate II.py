class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic or i - dic[nums[i]] > k:
                dic[nums[i]] = i
            else:
                return True
        return False