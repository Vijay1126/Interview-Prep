def indexEqualsValue(array):
   	
	left, right = 0, len(array)-1
	
	while left<=right:
		
		middleIndex = left + (right-left)//2
		middleValue = array[middleIndex]
		
		if middleValue<middleIndex:
			left = middleIndex+1
		elif middleValue == middleIndex and middleIndex == left:
			return middleIndex
		elif middleValue == middleIndex and array[middleIndex-1] < middleIndex-1:
			return middleIndex
		else:
			right = middleIndex-1
			
	return -1	
		
