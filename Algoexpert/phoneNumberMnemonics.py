def phoneNumberMnemonics(phoneNumber):
    mapping = {
		"1": ["1"],
		"2": ["a","b","c"],
		"3": ["d","e","f"],
		"4": ["g","h","i"],
		"5": ["j","k","l"],
		"6":["m","n","o"],
		"7":["p","q","r","s"],
		"8":["t","u","v"],
		"9":["w","x","y","z"],
		"0":["0"]
	}
	output = []
	return getMapping(phoneNumber, mapping, 0, [], output)

def getMapping(number, mapping, index, curr, output):
	if index == len(number):
		output.append("".join(curr))
	else:		
		digit = number[index]
		for letter in mapping[digit]:
			curr.append(letter)
			getMapping(number, mapping, index+1, curr, output)
			curr.pop()
		
	return output
		
