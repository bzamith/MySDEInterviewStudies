# Source: https://www.udemy.com/course/11-essential-coding-interview-questions/

# Problem: "Find the non-repeating char"

# Example: 
# aabcb -> c
# xxyz -> y
# aabbdbc -> d 

# Brute-force solution:
# For each char, loop and count (O(N^2))

# Approach:
# If we were concerned about usig extra space and the answer could be
# any char which count = 1, then we could sort the string (Solution2)
# Since it is not the case, we can use a hash table

# Complexity:
# O(N) time
# O(N) space

def nonRepeatingCharBestApproach(word): 
	auxHash = {}
	for i in range(len(word)):
		if not word[i] in auxHash:
			auxHash[word[i]] = 0
		auxHash[word[i]] += 1
	for i in range(len(word)):
		if auxHash[word[i]] == 1:
			return word[i]
	return None

def nonRepeatingChar(word): 
	word = list(word)
	word.sort()
	currSeq = 1
	currChar = word[0]
	for i in range(1, len(word)):
		if word[i] == currChar:
			currSeq += 1
		else:
			if currSeq == 1:
				return currChar
			else:
				currSeq = 1
				currChar = word[i]
	return None

if __name__ == "__main__":
	print(nonRepeatingCharBestApproach("aabbdbc"))
