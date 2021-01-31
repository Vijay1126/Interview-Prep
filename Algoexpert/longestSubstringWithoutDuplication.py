def longestSubstringWithoutDuplication(string):
    
	start = 0
	seen = set()
	end = 0
	output = ""
	length = 0
	while end<len(string):
		char = string[end]
		if char in seen:
			
			seen.remove(string[start])
			start+=1
			
		else:
			seen.add(char)
			end+=1
			if len(seen)>length:
				length = len(seen)
				output = string[start: end]
		
	return output
			
		
