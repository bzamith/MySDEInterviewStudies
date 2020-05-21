# Source: CS Dojo = https://www.youtube.com/watch?v=86CQq3pKSUw&t=576s

# Problem: "Find the maximum sum of a sub array"

# Example: 
#  [1,-3,2,1,-1] -> [2,1]

# Brute-force solution:
# Generate all possible subarrays (O(Nˆ2))

# Approach:
# Keep track of local and global optimals. If sum < 0, restart

# Complexity:
# O(N) time
# O(N) space (could improve it if I stored indices instead of the array)

def maxSumSubArray(array):
	if not array:
		return None
	if len(array) == 1:
		return array
	globalOptimal = [array[0]]
	globalSum = array[0]
	localSum = array[0]
	localOptimal = [array[0]]

	for i in range(1, len(array)):
		currSum = localSum + array[i]
		if currSum < 0:
			localSum = 0
			localOptimal = []
		if currSum >= localSum:
			localSum = currSum
			localOptimal.append(array[i])
		if localSum >= globalSum:
			globalSum = localSum
			globalOptimal = localOptimal
	return globalOptimal

if __name__ == "__main__":
	print(maxSumSubArray([1,-3,2,1,-1]))