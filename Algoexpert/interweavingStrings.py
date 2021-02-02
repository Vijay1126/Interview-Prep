def interweavingStrings(one, two, three):
    if len(one) + len(two) != len(three):
		return False
	
	return canInterweave(one, two ,three, 0 , 0, {})

def canInterweave (one, two , three, i, j, cache):
	if (i,j) in cache:
		return cache[(i,j)]
	k = i+j
	if k == len(three):
		return True
	
	if i <len(one) and one[i] == three[k]:
		cache[(i,j)] =  canInterweave(one, two , three, i+1, j, cache)
		if cache[(i,j)]:
			return True
	if j<len(two) and two[j] == three[k]:
		cache[(i,j)] = canInterweave(one, two, three, i, j+1, cache)	
		return cache[(i,j)] 
	
	return False	
		
	
	
	
