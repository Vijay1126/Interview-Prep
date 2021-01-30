def searchForRange(array, target):    
	return [binaryLeft(array, target),binaryRight(array, target)]

def binaryLeft(arr, target):
	
	left , right = 0, len(arr)-1
	
	while left<=right:
		
		mid = left + (right-left)//2
		
		if arr[mid] == target and (mid == left or arr[mid-1]!=target):
			return mid
		elif arr[mid]<target:
			left = mid+1
		else:
			right = mid-1
	return -1

def binaryRight(arr, target):
	
	left , right = 0, len(arr)-1
	
	while left<=right:
		
		mid = left + (right-left)//2
		
		if arr[mid] == target and (mid == right or arr[mid+1]!=target):
			return mid
		elif arr[mid]<=target:
			left = mid+1
		else:
			right = mid-1
	return -1
