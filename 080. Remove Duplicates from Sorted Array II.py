class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        slow = 0
        twice = True
        for fast in range(1, len(nums)):
            if nums[fast] == nums[slow] and twice:
                slow += 1
                nums[slow] = nums[fast]
                twice = False
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
                twice = True
        nums = nums[:(slow+1)]
        return (slow+1)