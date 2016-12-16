class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # dynamic programming
        # O(target*n) time, O(target) space
        number = [1]+[0]*target
        for current_target in range(1, target+1):
            for num in nums:
                if num <= current_target:
                    number[current_target] += number[current_target-num]
        return number[target]