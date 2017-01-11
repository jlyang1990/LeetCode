# n = p1**n1 * p2**n2 * ... * pk ** nk
# construct primeDic: O(pk+n1+...+nk) time if nk>1, O(pk**0.5+n1+...+nk) time if nk=1
# construct factorList: O(n1n2...nk) time
def allFactors(n):
	# construct primeDic
	primeDic = {}
	i = 2
	while i <= n**0.5:
		if n % i == 0:
			if i not in primeDic:
				primeDic[i] = 1
			else:
				primeDic[i] += 1
			n /= i
		else:
			i += 1
	if n > 1:
		primeDic[n] = 1
	# construct factorList
	result = [1]
	for prime in primeDic:
		factors = result[:]
		for i in range(1, primeDic[prime]+1):
			factors = [factor*prime for factor in factors]
			result += factors
	return result

