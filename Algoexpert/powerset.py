def powerset(array):
	output = []
    return getSubsets(array, output, [], 0)
def getSubsets(array, output, curr, index):
	output.append(curr[:])
	for i in range(index, len(array)):
		curr.append(array[i])
		getSubsets(array, output, curr, i+1)
		curr.pop()
	
	return output
		
	
	
