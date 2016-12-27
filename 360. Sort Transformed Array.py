class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        # O(n) time 
        if a == 0:
            result = [b*x+c for x in nums]
            if b < 0:
                result = result[::-1]
        else:
            result = []
            left, right = 0, len(nums)-1
            while left <= right:
                if abs(nums[left]+float(b)/(2*a)) >= abs(nums[right]+float(b)/(2*a)):
                    result.append(nums[left])
                    left += 1
                else:
                    result.append(nums[right])
                    right -= 1
            result = [a*x*x+b*x+c for x in result]
            if a > 0:
                result = result[::-1]
        return result