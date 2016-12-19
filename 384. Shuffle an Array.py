class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type size: int
        """
        self.nums = nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        from random import randint
        shuffle_nums = self.nums[:]
        n = len(self.nums)
        for i in range(n):
            temp = randint(i, n-1)
            shuffle_nums[i], shuffle_nums[temp] = shuffle_nums[temp], shuffle_nums[i]
        return shuffle_nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()