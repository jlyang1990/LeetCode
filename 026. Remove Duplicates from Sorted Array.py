class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # two pointers
        if not nums:
            return 0
        slow = 0
        fast = 1
        while fast < len(nums):
            while fast < len(nums) and nums[fast] == nums[slow]:
                fast += 1
            if fast < len(nums):
                slow += 1
                nums[slow] = nums[fast]
        nums = nums[:(slow+1)]
        return (slow+1)