# Source: https://www.youtube.com/watch?v=EYFcQRwcqk0

# Problem: "Find the K Most Frequent Elements in an Array"

# Example: 
#  [1,1,2,3,1,4,3,2,5]
#  k = 3 -> [1,2,3]

# Approach:
# Use a hash map to store the frequencies. Iterate over
# the hash map with a max heap (aka priority queue)
# To insert in heapq, create tuple, and negative because
# it is originally implemented as minHeap

# Complexity:
# O(N*log(k)) time
# O(N) space

import heapq

def kMostFrequentElements(array, k):
	if not array:
		return None
	if k > len(array):
		return None
	freq = {}
	heap = []
	resp = []
	for element in array:
		if not element in freq:
			freq[element] = 0
		freq[element] += 1
	for key in freq.keys():
		heapq.heappush(heap, (-freq[key],key)) 
	if k > len(heap):
		return None
	for i in range(k):
		resp.append(heapq.heappop(heap)[1])
		# heapq.nlargest(k, freq.keys(), key=freq.get) 
	return resp

if __name__ == "__main__":
	print(kMostFrequentElements([1,1,2,3,1,4,3,2,5],3))
	print(kMostFrequentElements([1,1,2,3,1,4,3,2,5,5,5,5,5],3))
	print(kMostFrequentElements([],3))
	print(kMostFrequentElements([1,1,2,3,1,4,3,2,5],8))
	