def findClosestValueInBst(tree, target):
    return findOutput(tree.value,target,tree)

def findOutput(closest, target, tree):
	if tree is None:
		return closest
	
	if abs(target - closest)>abs(tree.value-target):
		closest = tree.value
	if tree.value<target:
		return findOutput(closest, target,tree.right)
	elif tree.value>target:
		return findOutput(closest, target, tree.left)
	else:
		return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
