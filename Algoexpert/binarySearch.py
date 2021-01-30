def binarySearch(array, target):
    
	left, right = 0, len(array)-1
	
	while left<=right:
		mid = left + (right-left)//2
		
		if array[mid] == target:
			return mid
		elif array[mid]<target:
			left = mid+1
		else:
			right = mid-1
		
	return -1
