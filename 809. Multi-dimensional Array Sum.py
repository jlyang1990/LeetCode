def multiDimArray(array, dim):
	result = [0]
	multiDimArrayHelper(array, dim, 0, result, [])
	return result[0]

def multiDimArrayHelper(array, dim, start, result, index):
	if start == len(dim):
		result[0] += get(array, index)
	else:
		for i in range(dim[start]):
			multiDimArrayHelper(array, dim, start+1, result, index+[i])



def multiDim(dim):
	result = []
	multiDimHelper(dim, 0, result, [])
	return result

def multiDimHelper(dim, start, result, index):
	if start == len(dim):
		result.append(index)
	else:
		for i in range(dim[start]):
			multiDimHelper(dim, start+1, result, index+[i])