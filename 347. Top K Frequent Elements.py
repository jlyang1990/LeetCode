class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # quick sort
        def partition(nums, first, last):
            left = first+1
            right = last
            while left <= right:
                while left <= right and nums[left] <= nums[first]:
                    left += 1
                while left <= right and nums[right] >= nums[first]:
                    right -= 1
                if left <= right:
                    nums[left], nums[right] = nums[right], nums[left]
            nums[first], nums[right] = nums[right], nums[first]
            return right
            
        def topKFrequentHelper(nums, k, first, last):
            loc = partition(nums, first, last)
            if loc == len(nums) - k:
                return nums[loc:]
            elif loc < len(nums) - k:
                return topKFrequentHelper(nums, k, loc+1, last)
            else:
                return topKFrequentHelper(nums, k, first, loc-1)
                
        nums_dic = {}
        for i in nums:
            if i not in nums_dic:
                nums_dic[i] = 1
            else:
                nums_dic[i] += 1
        
        counts = []
        for j in nums_dic:
            counts.append(nums_dic[j])
        
        topK_counts = topKFrequentHelper(counts, k, 0, len(counts)-1)
        
        counts_dic = {}
        for i in topK_counts:
            if i not in counts_dic:
                counts_dic[i] = 1
            else:
                counts_dic[i] += 1
                
        topK_nums = []
        for j in nums_dic:
            if nums_dic[j] in counts_dic and counts_dic[nums_dic[j]] > 0:
                topK_nums.append(j)
                counts_dic[nums_dic[j]] -= 1
                
        return topK_nums