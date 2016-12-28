class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n, k = len(A), len(A[0]), len(B[0])
        ADic = [{} for i in range(m)]
        for i in range(m):
            for j in range(n):
                if A[i][j] != 0:
                    ADic[i][j] = A[i][j]
        print list(ADic)
        BDic = [{} for i in range(k)]
        for i in range(k):
            for j in range(n):
                if B[j][i] != 0:
                    BDic[i][j] = B[j][i]
        result = [[0]*k for i in range(m)]
        for i in range(m):
            for j in range(k):
                for index in ADic[i]:
                    if index in BDic[j]:
                        result[i][j] += ADic[i][index] * BDic[j][index]
        return result