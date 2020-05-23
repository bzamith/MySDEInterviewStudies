# Source: Cracking the Coding Interview, 17.20
# Source: https://www.youtube.com/watch?v=1CxyVdA_654

# Problem: "Continuous Median"

# Example: Numbers are randonly generated and passed to a method.
# Write a program to find and maintain the median value as new values
# are generated

# Brute-force approach: Sort the array each time and get the middle valeu

# Approach: Use a minHeap and a maxHeap. Keep balancing them

import heapq

class Solution():
	def __init__(self):
		self.heapMax = []
		self.heapMin = []
	def insert(self, element):
		if len(self.heapMax) == 0:
			self.heapMax.append(element*-1)
		elif len(self.heapMin) == 0:
			if element > -1*self.heapMax[0]:
				self.heapMin.append(element)
			else:
				curr = self.heapMax[0]*-1
				self.heapMin.append(curr)
				self.heapMax[0] = element*-1
		else:
			# self.heapMaxTop
			self.heapMaxTop = self.heapMax[0]*-1
			# self.heapMinTop
			self.heapMinTop = self.heapMin[0]
			if element <= self.heapMaxTop:
				heapq.heappush(self.heapMax, -1*element)
			else:
				heapq.heappush(self.heapMin, element)
			if len(self.heapMax) - len(self.heapMin) == 2:
				curr = heapq.heappop(self.heapMax)
				heap.heappush(self.heapMin, element*-1)
			elif len(self.heapMin) - len(self.heapMax) == 1:
				curr = heapq.heappop(self.heapMin)
				heapq.heappush(self.heapMax, element*-1)

	def getMedian(self):
		if len(self.heapMax) == 0:
			return None
		if len(self.heapMin) == 0:
			return self.heapMax[0]*-1
		totalSize = len(self.heapMax) + len(self.heapMin)
		if totalSize%2 == 0:
			return (self.heapMax[0]*-1 + self.heapMin[0])/2
		return self.heapMax[0]*-1

if __name__ == '__main__':
	sol = Solution()
	print(sol.getMedian())
	sol.insert(4)
	print(sol.getMedian())
	sol.insert(2)
	print(sol.getMedian())
	sol.insert(1)
	print(sol.getMedian())
	sol.insert(7)
	print(sol.getMedian())
	sol.insert(-2)
	print(sol.getMedian())