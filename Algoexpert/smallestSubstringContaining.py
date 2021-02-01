from collections import Counter, defaultdict
def smallestSubstringContaining(bigString, smallString):
    frequency = Counter(smallString)
	A = 0
	B = 0
	
	uniqueLetters = len(frequency)
	currCount = defaultdict(int)
	
	count = 0
	outputStr, outputLen = "", 9798798
	
	while B<len(bigString):
		currChar = bigString[B]
		currCount[currChar]+=1
		
		if currCount[currChar] == frequency[currChar]:
			count+=1
		if count == uniqueLetters:
			while count == uniqueLetters:
				startChar = bigString[A]
				currCount[startChar]-=1
				if currCount[startChar]<frequency[startChar]:
					count-=1
				A+=1
			if B-A+1<outputLen:
				outputLen = B-A+1
				outputStr = bigString[A-1:B+1]
		B+=1	
	return outputStr
