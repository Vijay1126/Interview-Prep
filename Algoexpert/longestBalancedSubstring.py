def longestBalancedSubstring(string):
    start = 0
	end = 0
	return max(getCount(string, 1),getCount( string, -1)) 

def getCount(string, step):
	openCount, closeCount = 0, 0
	index = 0 if step == 1 else len(string)-1
	openingBracket = "(" if step == 1 else ")"
	closingBracket = ")" if step == 1 else "("
	outputLen = 0
	while index>=0 and index<len(string):
		bracket = string[index]
		if bracket == openingBracket:
			openCount+=1
		else:
			closeCount+=1
		if openCount == closeCount:
			outputLen = max(outputLen, closeCount*2)
		if closeCount>openCount:
			closeCount = 0
			openCount = 0
		index+=step
		# print(count, string[start:end], end-start+1)
	return outputLen
		
		
