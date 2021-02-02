# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, multiplier = 1):
    total = 0
	
	for i in array:
		if type(i) is list:
			total += productSum(i, multiplier+1)
		else:
			total += i
		
	return total * multiplier
