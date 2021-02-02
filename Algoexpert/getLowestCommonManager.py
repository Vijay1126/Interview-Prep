def getLowestCommonManager(topManager, reportOne, reportTwo):
    
	return getOrgInfo(topManager, reportOne, reportTwo).lowest

def getOrgInfo(manager, A, B):
	num = 0
	for person in manager.directReports:
		orgInfo = getOrgInfo(person, A,B)
		if orgInfo.lowest:
			return orgInfo
		num+=orgInfo.num
	if manager == A or manager == B:
		num+=1
	lowest = manager if num == 2 else None
	return OrgInfo(num, lowest)

class OrgInfo:
	def __init__(self, num, lowest):
		self.num = num
		self.lowest = lowest
# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
