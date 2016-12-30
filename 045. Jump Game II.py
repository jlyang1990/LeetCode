class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # bfs
        # O(n) time
        if len(nums) <= 1:
            return 0
        level, i, currentMax, nextMax = 0, 0, 0, 0
        while i <= currentMax:  # node count of current level > 0
            level += 1
            while i <= currentMax:  # traverse current level, and update the maximum reach
                nextMax = max(nextMax, i+nums[i])
                if nextMax >= len(nums)-1:
                    return level
                i += 1
            currentMax = nextMax  # update current level by next level