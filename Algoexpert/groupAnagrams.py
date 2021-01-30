from collections import defaultdict
def groupAnagrams(words):
    all = defaultdict(list)
	
	for word in words:	
		all["".join(sorted(word))].append(word)
	return list(all.values())
