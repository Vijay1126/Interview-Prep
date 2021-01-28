def quickSort(array):
	quickSortHelper(array, 0, len(array)-1)
	return array
def quickSortHelper(arr, start , end):
	if start>=end:
		return 
	pivot = start
	left = pivot + 1
	right = end
	
	while left<=right:
		leftElement = arr[left]
		rightElement = arr[right]
		pivotElement = arr[pivot]
		if leftElement>pivotElement and rightElement<pivotElement:
			swap(arr, left, right)
		if leftElement<=pivotElement:
			left+=1
		if rightElement>=pivotElement:
			right-=1
		
	swap(arr, pivot, right)
	quickSortHelper(arr, start, right-1) #we exclude right most element cause we know that element is now sorted
	quickSortHelper(arr, right+1, end)


def swap(arr, left, right):
	arr[left], arr[right] = arr[right], arr[left]
	
	
		
	
	
