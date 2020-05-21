# Source: https://www.udemy.com/course/11-essential-coding-interview-questions/

# Problem: "Return the most frequently occurring item in an array"

# Example: 
#  [1,3,1,3,2,1] -> 1

# Brute-force solution:
# For each element, count the occurances (O(Nˆ2))

# Approach:
# Hash table

# Complexity:
# O(N) time
# O(N) space

def mostFrequent(array): 
	countHash = {}
	currMostFreq = None
	currHigherFreq = 0
	for element in array: 
		if not element in countHash:
			countHash[element] = 0
		countHash[element] = 1
		if countHash[element] > currHigherFreq:
			currHigherFreq = countHash[element]
			currMostFreq = element
	return currMostFreq

if __name__ == "__main__":
	print(mostFrequent([1,3,1,3,2,1]))
	print(mostFrequent([]))
