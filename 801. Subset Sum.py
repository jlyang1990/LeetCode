# Given a set of distinct numbers, find the number of combinations (duplicates not allowed) that sum to a particular value
# O(n*sum) time, O(sum) space 
def subsetSum(nums, sum):
    array = [1] + [0] * sum
    for num in nums:
        for i in range(sum, num-1, -1):
            array[i] += array[i-num]
    return array[sum]

# Given a set of distinct numbers, find all combinations (duplicates not allowed) that sum to a particular value
def subsetSumList(nums, sum):
	array = [[[]]] + [[]] * sum
	for num in nums:
		for i in range(sum, num-1, -1):
			if len(array[i-num]) > 0:
				array[i] = array[i] + [x+[num] for x in array[i-num]]
	return array[sum]


# Given a set of distinct numbers, find the number of combinations (duplicates allowed) that sum to a particular value
# O(n*sum) time, O(sum) space
# Compare with 377. Combination Sum IV 
def subsetSum(nums, sum):
    array = [1] + [0] * sum
    for num in nums:
        for i in range(num, sum+1):
            array[i] += array[i-num]
    return array[sum]

# Given a set of distinct numbers, find all combinations (duplicates allowed) that sum to a particular value
def subsetSumList(nums, sum):
	array = [[[]]] + [[]] * sum
	for num in nums:
		for i in range(num, sum+1):
			if len(array[i-num]) > 0:
				array[i] = array[i] + [x+[num] for x in array[i-num]]
	return array[sum]


# Given a set of numbers, find the number of combinations that sum to a particular value
def subsetSum(nums, sum):
	nums.sort()
	array = [1] + [0] * sum
	count = 1
	for n in range(1, len(nums)):
		if nums[n] == nums[n-1]:
			count += 1
			continue
		for i in range(sum, nums[n-1]-1, -1):
			for k in range(1, min(count, i//nums[n-1])+1):
				array[i] += array[i-nums[n-1]*k]
		count = 1
	for i in range(sum, nums[-1]-1, -1):
			for k in range(1, min(count, i//nums[-1])+1):
				array[i] += array[i-nums[-1]*k]
	return array[sum]

# Given a set of numbers, find all combinations that sum to a particular value
def subsetSumList(nums, sum):
	nums.sort()
	array = [[[]]] + [[]] * sum
	count = 1
	for n in range(1, len(nums)):
		if nums[n] == nums[n-1]:
			count += 1
			continue
		for i in range(sum, nums[n-1]-1, -1):
			for k in range(1, min(count, i//nums[n-1])+1):
				if len(array[i-nums[n-1]*k]) > 0:
					array[i] = array[i] + [x+[nums[n-1]]*k for x in array[i-nums[n-1]*k]]
		count = 1
	for i in range(sum, nums[-1]-1, -1):
			for k in range(1, min(count, i//nums[-1])+1):
				if len(array[i-nums[-1]*k]) > 0:
					array[i] = array[i] + [x+[nums[-1]]*k for x in array[i-nums[-1]*k]]
	return array[sum]
