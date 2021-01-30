def validIPAddresses(string):  
	output = []
	backtrack(string, [], output,0)	
	return output
def backtrack(string, curr, output, index):
	if index == len(string) and len(curr)==4:
		output.append(".".join(curr[:]))
	elif len(curr)<4:
		for i in range(index, min(index+4, len(string)+1)):
			toAdd = string[index:i]
			if toAdd and 0<=int(toAdd)<=255:
				if  len(toAdd)>1 and string[index]=="0":
					break
				curr.append(toAdd)
				backtrack(string, curr, output, i)
				curr.pop()
	return output
	
				
			
			
