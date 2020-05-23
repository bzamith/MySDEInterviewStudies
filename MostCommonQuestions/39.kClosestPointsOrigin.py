# Source: https://leetcode.com/problems/k-closest-points-to-origin/
# Source: https://www.youtube.com/watch?v=eaYX0Ee0Kcg

# Problem: "K Closest Points to Origin"

# Example: We have a list of points on the plane.
# Find the K closest points to the origin (0, 0).
# (Here, the distance between two points on a plane is the Euclidean distance.)

# Brute-force approach: For each, calculate distance and sort

# Approach: Use minHeap

import heapq, math

def kClosestPoints(points, K):
	if not points or not K or K < 0:
		return None
	if K > len(points):
		return points
	points = setDistance(points)
	heapq.heapify(points)
	resp = []
	for i in range(K):
		curr = heapq.heappop(points)
		resp.append([curr[1],curr[2]])
	return resp

def setDistance(points):
	for i in range(0,len(points)):
		distance = math.sqrt(pow(points[i][0],2)+pow(points[i][1],2))
		points[i] = [distance, points[i][0], points[i][1]]
	return points

if __name__ == '__main__':
	print(kClosestPoints([[1,3],[-2,2]], 1))
	print(kClosestPoints([[3,3],[5,-1],[-2,4]], 2))