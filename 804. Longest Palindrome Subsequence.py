# c[i, j] = 1, if i = j
# c[i, j] = c[i+1, j-1]+2, if Xi = Xj
# c[i, j] = max(c[i+1, j], c[i, j-1]), if Xi != Xj
# O(n^2) time, O(n^2) space (can be reduced to O(n) space if optimal solution is not recorded)
def lps(X):
	n = len(X)
	c = [[0]*n for i in range(n)]
	b = [[0]*n for i in range(n)]
	for i in range(n):
		c[i][i] = 1
		b[i][i] = "Common"
	for l in range(1, n):
		for i in range(n-l):
			j = i+l
			if X[i] == X[j]:
				c[i][j] = c[i+1][j-1]+2
				b[i][j] = "Common"
			else:
				if c[i+1][j] > c[i][j-1]:
					c[i][j] = c[i+1][j]
					b[i][j] = "Down"
				else:
					c[i][j] = c[i][j-1]
					b[i][j] = "Left"
	return c, b

def lpsPrint(b, X, i, j):
	if i > j:
		return
	if i == j:
		print(X[i], end = "")
	else:
		if b[i][j] == "Common":
			print(X[i], end = "")
			lpsPrint(b, X, i+1, j-1)
			print(X[i], end = "")
		elif b[i][j] == "Down":
			lpsPrint(b, X, i+1, j)
		else:
			lpsPrint(b, X, i, j-1)


X = "character"
X = "charracter"
c, b = lps(X)
print(c[0][len(X)-1])
lpsPrint(b, X, 0, len(X)-1)