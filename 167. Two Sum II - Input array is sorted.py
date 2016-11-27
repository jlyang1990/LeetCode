class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # if numbers[i]+numbers[j]>target, then numbers[k]+numbers[j]>target, k=i+1,...,j-1, thus exclude them
        # the next step is to investigate numbers[i]+numbers[j-1]
        left = 0
        right = len(numbers)-1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1