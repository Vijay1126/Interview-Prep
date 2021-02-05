def sunsetViews(buildings, direction):
    # Write your code here.
    output = []
	i = 0 if direction == "WEST" else len(buildings)-1
	increment = 1 if i == 0 else -1
	stack = []
	currMax = -10000
	while i>=0 and i<len(buildings):
		currBuilding = buildings[i]
		if currMax<currBuilding:
			currMax = max(currMax, currBuilding)
			stack.append(currBuilding)
			output.append(i)
		i += increment
	
	if increment == -1: output = output[::-1]
	return output
