# Source: https://www.youtube.com/watch?v=VX2oZkDJeGA

# Problem: "Find circle in array"

# Example: 
#  A value in the array indicates the next position to go
#  [1,2,1,3,4,8]

# Questions:
# 1. Are we always going to start at the first index of the array? Yes
# 2. A number out of bounds indicate that the circle has stopped.

# Approach:
# Use hash map to store positions visited. When you go to a already
# seen position, stop (Solution 2). Use runner technique (Solution 1).

# Complexity:
# O(N) time 
# O(1) space

def findCircleArrayBestApproach(array):
	if not array:
		return None
	slow = fast = 0
	while fast < len(array):
		slow = array[slow]
		fast = array[array[slow]]
		if slow == fast:
			return True
		if len(array) <= slow < 0 or len(array) <= fast < 0:
			return False
	return False

def findCircleArray(array):
	if not array:
		return None
	visited = {}
	for i in range(len(array)):
		if array[i] in visited:
			return True
		else:
			visited[array[i]] = True
	return False


if __name__ == '__main__':
	print(findCircleArrayBestApproach([1,2,1,3,4,8]))
	print(findCircleArrayBestApproach([1,2,3,4,5,6]))
	print(findCircleArray([1,2,1,3,4,8]))
	print(findCircleArray([1,2,3,4,5,6]))