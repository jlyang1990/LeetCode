class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        # divide and conquer
        if input.isdigit():
            return [int(input)]
        result = []
        for i in range(len(input)):
            if input[i] in "+-*":
                result1 = self.diffWaysToCompute(input[:i])
                result2 = self.diffWaysToCompute(input[i+1:])
                for j in result1:
                    for k in result2:
                        if input[i] == "+":
                            result.append(j+k)
                        if input[i] == "-":
                            result.append(j-k)
                        if input[i] == "*":
                            result.append(j*k)
        return result