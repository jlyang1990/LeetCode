# Given a chain (A1, A2, ..., An) of n matrices, where matrix Ai has dimension pi-1xpi.
# Fully parenthesize the product A1A2...An in a way that minimizes the number of scalar multiplications.
# m[i, j] = 0, if i = j
# m[i, j] = min_{i<=k<j} m[i, k]+m[k+1, j]+pi-1pkpj, if i < j
# O(n^3) time, O(n^2) space
def matrixChain(p):
	n = len(p)-1
	m = [[float("inf")]*n for i in range(n)]
	s = [[0]*n for i in range(n)]
	for i in range(n):
		m[i][i] = 0
	for l in range(1, n):
		for i in range(n-l):
			j = i+l
			for k in range(i, j):
				temp = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]
				if temp < m[i][j]:
					m[i][j] = temp
					s[i][j] = k
	return m, s

def matrixChainPrint(s, i, j):
	if i == j:
		print(i+1, end = "")
	else:
		print("(", end = "")
		matrixChainPrint(s, i, s[i][j])
		matrixChainPrint(s, s[i][j]+1, j)
		print(")", end = "")


p = [30, 35, 15, 5, 10, 20, 25]
m, s = matrixChain(p)
print(m[0][len(p)-2])
matrixChainPrint(s, 0, len(p)-2)