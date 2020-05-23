# Problem: K Smallest Elements in Unsorted Array

# Example: Given an array and a number k where k is smaller than size of 
# array, we need to find the k smallest elements in the given array. 
# It is given that ll array elements are distinct.

# Brute-force Solution: Sort the array and iterate k times

# Approach: Use min heap

# Complexity
# O(n + k*log(N)) -> time
# O(N) -> space

import heapq

def kSmallest(array, k):
	if not array or k > len(array):
		return None
	heapq.heapify(array) # in-place
	resp = []
	for i in range(k):
		resp.append(heapq.heappop(array))
	return resp

if __name__ == '__main__':
	print(kSmallest([1,4,3,0,-2,7],3))