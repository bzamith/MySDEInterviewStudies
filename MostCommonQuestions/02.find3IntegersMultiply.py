# Source: https://www.udemy.com/course/11-essential-coding-interview-questions/

# Problem: "Find three integers that multiply to k"

# Example: 
#  [2,2,1,6,5,40,-1], 20 -> [2,2,5]

# Brute-force solution:
# Check any possible triplet (O(Nˆ3))

# Approach:
# Sort the array, fix the first element and use the two pointers technique

# Complexity:
# O(N*log(N)) time (sorting)
# O(1) space

def mostFrequent(array): 
	if not array:
		return None
	for i in range(0, arraySize-2): 
		left = i + 1 
		right = arraySize-1 
		while (left < right): 
			mult = array[i] * array[left] * array[right]
			if mult == k:  
				return [array[i], array[left], array[right]]
			elif mult < k: 
				left += 1
			else:
				right -= 1
	return None

if __name__ == "__main__":
	print(find3IntegersMulitply([2,3,1,5,-20,-1], 20))
	print(find3IntegersMulitply([],10))


