def numberOfBinaryTreeTopologies(n):
    cache = [1]
	
	for numberOfNodes in range(1,n+1):
		total = 0
		for leftSize in range(numberOfNodes):
			rightSize = numberOfNodes-1-leftSize
			leftNodes = cache[leftSize]
			rightNodes = cache[rightSize]
			total += leftNodes*rightNodes
		cache.append(total)
	
	return(cache[-1])
	
	
