def shortenPath(path):
    absolutePath = path[0] == "/"
	tokens = filter( valid, path.split("/"))
	stack = []
	if absolutePath:
		stack.append("")
	for token in tokens:
		if token == "..":
			if not stack or stack[-1] =="..":
				stack.append(token)
			elif stack[-1]!="":
				stack.pop()
		else:
			stack.append(token)
	if len(stack) == 1 and stack[-1] == "":
		return "/"
	return "/".join(stack)
	
def valid(word):
	return len(word)>0 and word!="."
