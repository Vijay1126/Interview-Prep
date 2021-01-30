def findThreeLargestNumbers(array):
    output = [None, None, None]
	
	for num in array:
		updateLargest(output, num)
	
	return output

def updateLargest(output, n):
	#go from the biggest to the smallest	
	for i in ([2,1,0]):
		if output[i] == None or output[i]<n:
			shift(output, i, n)
			break
def shift(output, index, number):
	for i in range(index+1):
		if i == index:
			output[i] = number
		else:
			output[i] = output[i+1]
		
		
