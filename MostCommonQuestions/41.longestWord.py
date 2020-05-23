# Source: Cracking the Coding Interview, 17.15
# Source: https://www.youtube.com/watch?v=QGVCnjXmrNg

# Problem: "Longest Word"

# Example: Given a list of words, write a program to find the longest
# word made of other words elements in the list
# wordslist = ["cat", "cats", "dog", "catsdog"]
# should return "catsdog"

# Approach: Hash + Recursion + Dynamic Programming

def getLongestCombinedWord(array):
	hashMap = {}
	for string in array:
		hashMap[string] = True
	array.sort(key=len, reverse=True)
	for string in array:
		if canBuildWord(string, True, hashMap):
			return string
	return None

def canBuildWord(string, isOriginalWord, hashMap):
	if string in hashMap and not isOriginalWord:
		return hashMap[string]
	for i in range(1, len(string)):
		left = string[0:i]
		right = string[i:]
		if left in hashMap and hashMap[left] == True and canBuildWord(right, False, hashMap):
			return True
	hashMap[string] = False
	return False

if __name__ == '__main__':
	print(getLongestCombinedWord(["cat", "cats", "dog", "catsdog"]))
