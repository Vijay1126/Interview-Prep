def quickselect(array, k):
	return quickSortHelper(array, 0, len(array)-1, k-1)

def quickSortHelper(array, left, right, position):
	while True:
		if left>right:
			raise Exception("Invalid Array")

		pivot = left
		start = pivot + 1
		end = right

		while start<=end:
			startElement, pivotElement, endElement = array[start], array[pivot], array[end]

			if startElement<=pivotElement:
				start+=1
			if endElement>=pivotElement:
				end-=1
			if startElement>pivotElement and endElement<pivotElement:
				swap(array, start , end)

		swap(array, pivot, end)
		if end == position:
			return array[position]
		elif end<position:
			left = end+1
		else:
			right = end-1

def swap(arr, left, right):
	arr[left], arr[right] = arr[right], arr[left]
		

		
		
