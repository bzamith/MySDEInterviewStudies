# Source: https://www.udemy.com/course/11-essential-coding-interview-questions/

# Problem: "Validate Parenthesis in a String"

# Example: 
#  If a parenthesis was opened, the corresponding parenthesis must be closed
#  in the correct order

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

import queue

def validateParenthesisBestApproach(string):
	stack = queue.LifoQueue()
	parenthesisOpen = ['(','[','{']
	parenthesisClose = [')',']','}']
	for char in string:
		if char in parenthesisOpen:
			stack.put(char)
		elif char in parenthesisClose:
			if stack.empty():
				return False
			currOpen = stack.get()
			indCurrOpen = parenthesisOpen.index(currOpen)
			if char != parenthesisClose[indCurrOpen]:
				return False
	if not stack.empty():
		return False
	return True

def validateParenthesis(string):
	count = 0
	for char in string:
		if char == '(':
			count += 1
		elif char == ')':
			count -= 1
		if count < 0:
			return False
	if count != 0:
		return False
	return True

if __name__ == "__main__":
	print(validateParenthesisBestApproach("abc(){()}[]"))
	print(validateParenthesisBestApproach("("))
	print(validateParenthesisBestApproach("}"))
	print(validateParenthesisBestApproach("abd((([)]"))
	print(validateParenthesis("2+(1*(3-2)+7)"))
	print(validateParenthesis("(((()a))"))
	print(validateParenthesis("(((()a))"))
	print(validateParenthesis(")()("))