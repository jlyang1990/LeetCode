class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # incorparate 3Sum and 2Sum
        # O(n^3) time
        nums.sort()
        result = []
        for first in range(len(nums)):
            if first > 0 and nums[first] == nums[first-1]:
                continue
            for second in range(first+1, len(nums)):
                if second > first+1 and nums[second] == nums[second-1]:
                    continue
                left, right = second+1, len(nums)-1
                while left < right:
                    if nums[left]+nums[right] == target-nums[first]-nums[second]:
                        result.append([nums[first], nums[second], nums[left], nums[right]])
                        while left < right and nums[left+1] == nums[left]:
                            left += 1
                        while left < right and nums[right-1] == nums[right]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif nums[left]+nums[right] < target-nums[first]-nums[second]:
                        left += 1
                    else:
                        right -= 1
        return result