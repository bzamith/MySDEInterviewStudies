# Source: https://www.youtube.com/watch?v=5o-kdjv7FD0

# Problem: "Recursive Staircase Problem"

# Example: 
#  There are n stairs, a person standing at the bottom wants 
#  to reach the top. The person can climb either 1 stair or 2 
#  stairs at a time. Count the number of ways, the person can reach the top.
#  totalSteps = 3, climbTypes = [1,2]
#  return 3 ([1,1,1], [1,2], [2,1])

# Brute-force solution:
# Recursion. Bottom-up

# Approach:
# Use Dynamic Programming to avoid recalculating the same stuff

# Complexity:
# O(N) time
# O(N) space

def recursiveStaircaseBestApproach(totalSteps, climbTypes):
	memo = [None for i in range(totalSteps+1)]
	def recursiveStaircaseHelper(currStep):
		if currStep > totalSteps:
			return 0
		if currStep == totalSteps:
			return 1
		if memo[currStep] is not None:
			return memo[currStep]
		resp = 0
		for climbType in climbTypes:
			resp += recursiveStaircaseHelper(currStep + climbType)
		memo[currStep] = resp
		return resp
	return recursiveStaircaseHelper(0)

def recursiveStaircase(totalSteps, climbTypes):
	def recursiveStaircaseHelper(currStep):
		if currStep > totalSteps:
			return 0
		if currStep == totalSteps:
			return 1
		resp = 0
		for climbType in climbTypes:
			resp += recursiveStaircaseHelper(currStep + climbType)
		return resp
	return recursiveStaircaseHelper(0)

if __name__ == "__main__":
	print(recursiveStaircase(2, [1,2]))
	print(recursiveStaircaseBestApproach(2, [1,2]))
	print("---------------------------------------")
	print(recursiveStaircase(3, [1,2]))
	print(recursiveStaircaseBestApproach(3, [1,2]))
	print("---------------------------------------")
	print(recursiveStaircase(4, [1,2,5]))
	print(recursiveStaircaseBestApproach(4, [1,2,5]))