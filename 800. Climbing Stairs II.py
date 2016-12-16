# n stairs, exactly k steps, every step: 1, 2 or 3 stairs
# O(nk) time, O(n) space
def climbStairs(n, k):
	if n < 3:
		count = [1]*n
	else: 
		count = [1]*3+[0]*(n-3)
	for i in range(k-1):
		for j in range(n-1, -1, -1):
			if j == 0:
				count[j] = 0
			elif j == 1:
				count[j] = count[j-1]
			elif j == 2:
				count[j] = count[j-1] + count[j-2]
			else:
				count[j] = count[j-1] + count[j-2] + count[j-3]
	return count[n-1]


# n stairs, at most k steps, every step: 1, 2 or 3 stairs
# O(nk) time, O(n) space
def climbStairs(n, k):
	if n < 3:
		count = [1]*n
	else: 
		count = [1]*3+[0]*(n-3)
	count_total = count[n-1]
	for i in range(k-1):
		for j in range(n-1, -1, -1):
			if j == 0:
				count[j] = 0
			elif j == 1:
				count[j] = count[j-1]
			elif j == 2:
				count[j] = count[j-1] + count[j-2]
			else:
				count[j] = count[j-1] + count[j-2] + count[j-3]
		count_total += count[n-1]
	return count_total