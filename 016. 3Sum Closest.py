class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        minDiffUp = float("inf")
        minDiffDown = float("inf")
        for first in range(len(nums)):
            if first > 0 and nums[first] == nums[first-1]:
                continue
            left, right = first+1, len(nums)-1
            while left < right:
                if nums[left] + nums[right] == target-nums[first]:
                    return target
                elif nums[left] + nums[right] < target-nums[first]:
                    minDiffDown = min(minDiffDown, target-nums[left]-nums[right]-nums[first])
                    left += 1
                else:
                    minDiffUp = min(minDiffUp, nums[left]+nums[right]+nums[first]-target)
                    right -= 1
        return target-minDiffDown if minDiffDown < minDiffUp else target+minDiffUp