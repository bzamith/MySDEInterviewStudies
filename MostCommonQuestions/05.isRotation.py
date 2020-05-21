# Source: https://www.udemy.com/course/11-essential-coding-interview-questions/

# Problem: "Check if one array is a rotation of another"

# Example: 
#  [1,2,3,4,5,6,7],[4,5,6,7,1,2,3] -> True

# Questions:
# 1. Are there duplicates? No

# Brute-force solution:
# Generate all rotations and compare

# Approach:
# Fix the first one, find diff.
# Compare each A[i] with A[diff+i]. If diff + i >= len(A) 
# use diff + i - len(A) instead

# Complexity:
# O(N) time
# O(1) space

def isRotation(arrayA, arrayB): 
	arraySize = len(arrayA)
	if not arraySize == len(arrayB):
		return False

	for diff in range(arraySize):
		if arrayB[diff] == arrayA[0]:
			break
	if arrayA[0] != arrayB[diff]:
		return False
	
	for i in range(arraySize):
		indB = i + diff 
		if indB >= arraySize:
			indB -= arraySize
		if arrayA[i] != arrayB[indB]:
			return False
	return True

if __name__ == "__main__":
	print(isRotation([1,2,3,4,5,6,7],[4,5,6,7,1,2,3]))
