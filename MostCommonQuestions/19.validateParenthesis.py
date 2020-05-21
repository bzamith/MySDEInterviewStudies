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