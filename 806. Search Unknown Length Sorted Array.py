# O(logn) time
def searchUnknownLengthSortedArray(nums, target):
	lower, upper = 0, 1
	done = False
	while not done:
		try:
			if nums[upper] == target:
				return upper
			elif nums[upper] > target:
				done = True
			else:
				lower, upper = upper, upper*2
		except IndexError:
			done = True
	while lower <= upper:
		mid = (lower+upper)//2
		try:
			if nums[mid] == target:
				return mid
			elif nums[mid] > target:
				upper = mid-1
			else:
				lower = mid+1
		except IndexError:
			upper = mid-1
	return -1