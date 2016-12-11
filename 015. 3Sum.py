class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # method 1: dfs
        nums.sort()
        result = []
        self.dfs(nums, 0, 3, 0, result, [])
        return result
       
    def dfs(self, nums, target, k, start, result, triplet):
        if target == 0 and k == 0:
            result.append(triplet)
        if k > 0:
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                self.dfs(nums, target-nums[i], k-1, i+1, result, triplet+[nums[i]])

        # method 2
        # for each possible first element, apply 2Sum
        # O(n^2) time
        nums.sort()
        result = []
        for first in range(len(nums)):
            if first > 0 and nums[first] == nums[first-1]:
                continue
            left, right = first+1, len(nums)-1
            while left < right:
                if nums[left] + nums[right] == -nums[first]:
                    result.append([nums[first], nums[left], nums[right]])
                    while left < right and nums[left+1] == nums[left]:
                        left += 1
                    while left < right and nums[right-1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < -nums[first]:
                    left += 1
                else:
                    right -= 1
        return result