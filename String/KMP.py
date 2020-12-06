def knuthMorrisPrattAlgorithm(string, substring):
    pattern = buildPattern(substring)
	return doesMatch(string, substring, pattern)

def buildPattern(array):
	i, j = 1, 0
	pattern = [-1 for i in range(len(array))]
	while i<len(array):
		if array[j]==array[i]:
			pattern[i] = j
			i+=1
			j+=1
		elif j>0:
			j = pattern[j-1]+1
		else:
			i+=1
	return pattern

def doesMatch(string, substring, pattern):
	i, j = 0, 0
	while i+len(substring)-j<=len(string):
		if string[i]==substring[j]:
			if j == len(substring)-1:
				return True
			i+=1
			j+=1
		elif j>0:
			j = pattern[j-1]+1
		else:
			i+=1
	return False
		
			
	
			
