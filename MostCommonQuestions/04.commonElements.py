# Source: https://www.udemy.com/course/11-essential-coding-interview-questions/

# Problem: "Find common elements in two sorted arrays"

# Example: 
#  [2,4,1,6,5,40,-1], [2,3,7,1,-1,0]-> [2,1,-1]

# Questions:
# 1. Are there duplicates? No
# 2. Do they have the same size? No

# Brute-force solution:
# Check each pair (O(N*M))

# Approach:
# I could use a hash map to store elements from one array and iterate over the
# other array, searching in the hash map. This could be a good approach if the 
# arrays weren't already sorted. Since they are, I can have space complexity O(1)
# by using two pointers strategy

# Complexity:
# O(max(N,M)) time
# O(1) space

def commonElementsBestApproach(arrayA, arrayB): 
	if not arrayA or not arrayB:
		return None
	resp = []
	a = 0
	b = 0
	while a < len(arrayA) and b < len(arrayB):
		if arrayA[a] == arrayB[b]:
			resp.append(arrayA[a])
			a += 1
			b += 1
		elif arrayA[a] > arrayB[b]:
			b += 1
		else:
			a += 1
	return resp

def commonElements(arrayA, arrayB): 
	arrayAHash = {}
	resp = []
	for element in arrayA:
		arrayAHash[element] = True
	for element in arrayB:
		if element in arrayAHash:
			resp.append(element)
	return resp

if __name__ == "__main__":
	print(commonElementsBestApproach([1,3,4,6,7,9],[1,2,4,5,9,10]))
