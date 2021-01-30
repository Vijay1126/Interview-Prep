def shiftedBinarySearch(nums, target):
    left = 0
	right = len(nums)-1
	
	while left<=right:
		
		mid = left + (right-left)//2
		if nums[mid] == target:
			return mid
		if nums[left]<nums[mid]:
			#left side is sorted
			if nums[left]<=target<nums[mid]:
				right = mid-1
			else:
				left = mid+1
		else:
			#right side is sorted
			if nums[mid]<target<=nums[right]:
				left = mid+1
			else:
				right = mid-1
		
	return -1
