# Source: https://www.youtube.com/watch?v=p0VD9Fdlx5A

# Problem: "Reverse the array in place"

# Example: 
#  [0,1,2,3,4,5,6] -> [6,5,4,3,2,1,0]
#  [1,2,3,4,5,6] -> [6,5,4,3,2,1]

# Brute-force solution:
# Use stack. Or copy array and iterate backwards. Not in-place, though.

# Approach:
# Two-pointers strategy

# Complexity:
# O(N) time (actually, O(N/2))
# O(1) space

def reverseArrayInPlace(array):
	if not array:
		return None
	left = 0
	right = len(array) - 1
	while right > left:
		aux = array[left]
		array[left] = array[right]
		array[right] = aux
		left += 1
		right -= 1
	return array

if __name__ == '__main__':
	print(reverseArrayInPlace([0,1,2,3,4,5,6]))
	print(reverseArrayInPlace([1,2,3,4,5,6]))