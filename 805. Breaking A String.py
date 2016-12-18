# c[i, j] = Li, if i = j
# c[i, j] = min_{i<=k<j} c[i, k]+c[k+1, j]+(Li+...+Lj)
# O(n^3) time, O(n^2) space
def breakingAString(L):
	n = len(L)
	cumL = [0]+L
	for i in range(n):
		cumL[i+1] = cumL[i]+cumL[i+1]
	c = [[float("inf")]*n for i in range(n)]
	b = [[0]*n for i in range(n)]
	for i in range(n):
		c[i][i] = 0
	for l in range(1, n):
		for i in range(n-l):
			j = i+l
			for k in range(i, j):
				temp = c[i][k] + c[k+1][j] + cumL[j+1] - cumL[i]
				if temp < c[i][j]:
					c[i][j] = temp
					b[i][j] = k
	return c, b

def breakingAStringPrint(b, i, j):
	if i == j:
		return
	print(b[i][j]+1, end = "")
	breakingAStringPrint(b, i, b[i][j])
	breakingAStringPrint(b, b[i][j]+1, j)


L = [2, 6, 2, 10]
c, b = breakingAString(L)
print(c[0][len(L)-1])
breakingAStringPrint(b, 0, len(L)-1)
