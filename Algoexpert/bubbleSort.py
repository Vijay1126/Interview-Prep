def bubbleSort(arr):
    
	isSorted = False
	
	counter = 0
	while not isSorted:
		isSorted = True
		for i in range(len(arr)-1-counter):
			
			if arr[i]>arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]
				isSorted = False
		counter+=1
		
	return arr


