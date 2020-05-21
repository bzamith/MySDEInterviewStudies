# Source: https://www.udemy.com/course/11-essential-coding-interview-questions/

# Problem: "Find two integers that multiply to k"

# Example: 
#  [2,4,1,6,5,40,-1], 20 -> [4,5]

# Questions:
# 1. Are there duplicates? Yes
# 2. Are there negative numbers? Yes

# Brute-force solution:
# Check any possible pairs (O(Nˆ2))

# Approach:
# Use a set() (which is a hash), look back

# Complexity:
# O(N) time
# O(N) space

def findIntegersMultiply(array, k):
	if not array:
		return None
	visitedNumbers = set()
	for number in array:
		diff = k/number
		if diff in visitedNumbers:
			return [diff, number]
		else:
			visitedNumbers.add(number)
	return None

if __name__ == "__main__":
	print(findIntegersMultiply([2,4,1,6,-20,-1], 20))
	print(findIntegersMultiply([],10))