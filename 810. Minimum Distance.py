#Given three sorted arrays A[], B[] and C[], find 3 elements i, j and k from A, B and C respectively such that 
#max(abs(A[i] – B[j]), abs(B[j] – C[k]), abs(C[k] – A[i])) is minimized. Here abs() indicates absolute value.
#Example: 
#Input: A[] = {1, 4, 10}  B[] = {2, 15, 20} C[] = {10, 12} Output: 10 15 10。 10 from A, 15 from B and 10 from C.
#Input: A[] = {20, 24, 100} B[] = {2, 19, 22, 79, 800} C[] = {10, 12, 23, 24, 119} Output: 24 22 23。24 from A, 22 from B and 23 from C.

# 244. Shortest Word Distance II with three words
# O(nA+nB+nC) time
def minDistance(A, B, C):
	i, j, k = 0, 0, 0
	minDist = float("inf")
	result = []
	while i < len(A) and j < len(B) and k < len(C):
	# if i = len(A)-1 and A[i] is the smallest, no further smaller minDist and the search is over, so the next i = len(A) we break
		curDist = max(abs(A[i]-B[j]), abs(B[j]-C[k]), abs(C[k]-A[i]))
		if curDist < minDist:
			minDist = curDist
			result = [A[i], B[j], C[k]]
		if A[i] <= B[j] and A[i] <= C[k]:
			i += 1
		elif B[j] <= A[i] and B[j] <= C[k]:
			j += 1
		else:
			k += 1
	return result


minDistance([1,4,10], [2,15,20], [10,12])
minDistance([20,24,100], [2,19,22,79,800], [10,12,23,24,119])
