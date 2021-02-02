from itertools import combinations
def getPermutations(array):
    if not array:
		return array
	
	output = []
	permute(output, array, index = 0)
	return output
def permute(output, array, index):
	if index == len(array):
		output.append(array[:])
	else:
		for i in range(index, len(array)):
			array[index], array[i] =  array[i], array[index]
			permute(output, array, index+1)
			array[index], array[i] =  array[i], array[index]
	return output
			
		
0
