# Source: https://www.udemy.com/course/11-essential-coding-interview-questions/

# Problem: "One Away Strings"
# 3 operations: 
# - Change, abcde -> abfde
# - Delete, abcde -> abde
# - Insert, abde -> abcde
# Return if they are one edit away

# Questions:
# 1. What should I return if they are equal? True

# Approach:
# If abs(len(s1) - len(s2)) >= 2 -> return False
# If lengths are equal, check if it is one change away
# If lengths are different, check if it is one insertion away from smaller
# to bigger one. It is the same as checking if it is one deletion away from
# bigger to smaller

def isOneAwayStrings(s1, s2): 
	if not s2 or not s2:
		return False
	size1 = len(s1)
	size2 = len(s2)
	if abs(size1 - size2) > 1:
		return False
	if size1 == size2:
		return isOneAwayChange(s1, s2)
	else:
		return isOneAwayInsertDelete(s1, s2)

def isOneAwayChange(s1, s2):
	if not len(s1) == len(s2):
		return False
	countDiff = 0
	for i in range(len(s1)):
		if not s1[i] == s2[i]:
			countDiff += 1
	return (countDiff <= 1)

def isOneAwayInsertDelete(s1, s2):
	if abs(len(s1) - len(s2)) > 1:
		return False
	if len(s1) > len(s2):
		bigger = s1
		smaller = s2
	else:
		bigger = s2
		smaller = s1
	countDiff = 0
	i = 0
	while i < len(smaller):
		if bigger[i + countDiff] == smaller[i]:
			i += 1
		else:
			countDiff += 1
	return (countDiff <= 1)

if __name__ == "__main__":
	print(isOneAwayStrings("abcde", "abcd"))  # should return True
	print(isOneAwayStrings("abde", "abcde"))  # should return True
	print(isOneAwayStrings("a", "a"))  # should return True
	print(isOneAwayStrings("abcdef", "abqdef"))  # should return True
	print(isOneAwayStrings("abcdef", "abccef"))  # should return True
	print(isOneAwayStrings("abcdef", "abcde"))  # should return True
	print(isOneAwayStrings("aaa", "abc"))  # should return False
	print(isOneAwayStrings("abcde", "abc"))  # should return False
	print(isOneAwayStrings("abc", "abcde"))  # should return False
	print(isOneAwayStrings("abc", "bcc"))  # should return False