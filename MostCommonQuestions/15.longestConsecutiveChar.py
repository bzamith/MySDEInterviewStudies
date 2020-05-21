# Source: CS Dojo = https://www.youtube.com/watch?v=qRNB8CV3_LU

# Problem: "Return the longest consecutive char"

# Example: 
#  AABCDDBBBEA -> {'B':3}

# Questions:
# 1. Does the case (lower or upper) matters? Yes

# Brute-force solution:
# Not a brute force solution actually, but using a hash map is
# unnecessary

# Approach:
# Keep track of the previous one and global

# Complexity:
# O(N) time
# O(1) space

def longestConsecutiveChar(string):
	if not string:
		return None
	if len(string) == 1:
		return {string : 1}
	globalChar = localChar = string[0]
	globalCount = localCount = 1
	for i in range(1, len(string)):
		if string[i] == string[i-1]:
			localCount += 1
		else:
			localCount = 1
			localChar = string[i]
		if localCount > globalCount:
				globalCount = localCount
				globalChar = localChar
	return {globalChar : globalCount}
	
if __name__ == "__main__":
	print(longestConsecutiveChar("aabcddbbbe"))
	print(longestConsecutiveChar("a"))