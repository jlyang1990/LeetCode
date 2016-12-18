# c[i, j] = 0, if i = 0 or j = 0
# c[i, j] = c[i-1, j-1]+1, if Xi = Yj
# c[i, j] = max(c[i-1, j], c[i, j-1]), if Xi != Yj
# O(mn) time, O(mn) space (can be reduced to O(n) space if optimal solution is not recorded)
def lcs(X, Y):
	m, n = len(X), len(Y)
	c = [[0]*(n+1) for i in range(m+1)]
	b = [[0]*n for i in range(m)]
	for i in range(m):
		for j in range(n):
			if X[i] == Y[j]:
				c[i+1][j+1] = c[i][j]+1
				b[i][j] = "Common"
			else:
				if c[i][j+1] > c[i+1][j]:
					c[i+1][j+1] = c[i][j+1]
					b[i][j] = "Up"
				else:
					c[i+1][j+1] = c[i+1][j]
					b[i][j] = "Left"
	return c, b

def lcsPrint(b, X, i, j):
	if i < 0 or j < 0:
		return
	if b[i][j] == "Common":
		lcsPrint(b, X, i-1, j-1)
		print(X[i], end = "")
	elif b[i][j] == "Up":
		lcsPrint(b, X, i-1, j)
	else:
		lcsPrint(b, X, i, j-1)


X = "ABCBDAB"
Y = "BDCABA"
c, b = lcs(X, Y)
print(c[len(X)][len(Y)])
lcsPrint(b, X, len(X)-1, len(Y)-1)