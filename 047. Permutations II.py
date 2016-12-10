class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # method 1
        result = [[]]
        for insert_index in range(len(nums)):
            temp = []
            for element in result:
                for insert_loc in range(insert_index+1):
                    temp.append(element[:insert_loc] + [nums[insert_index]] + element[insert_loc:])
                    # think about creating [1,2,1,2,1,2] by add 2
                    # there are three cases: [1,_,1,2,1,2], [1,2,1,_,1,2], [1,2,1,2,1,_] yield the same result
                    # only keep the case where 2 is added as the first 2, i.e., stop adding 2 when we meet 2
                    if insert_loc < insert_index and nums[insert_index] == element[insert_loc]:
                        break
            result = temp
        return result

        # method 2: dfs
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        result = []
        self.dfs(dic, result, [])
        return result
        
    def dfs(self, dic, result, permutation):
        if len(dic) == 0:
            result.append(permutation)
        else:
            for i in dic:
                dic_copy = dic.copy()
                dic_copy[i] -= 1
                if dic_copy[i] == 0:
                    del dic_copy[i]
                self.dfs(dic_copy, result, permutation+[i])