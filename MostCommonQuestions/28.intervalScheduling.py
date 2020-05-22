# Source: https://www.youtube.com/watch?v=hVhOeaONg1Y
# Source: https://leetcode.com/problems/non-overlapping-intervals/

# Problem: "Interval Scheduling Maximization"

# Example: 
#   Given a collection of intervals, find the minimum number of 
#   intervals you need to remove to make the rest of the intervals non-overlapping. 
#   Input: [[1,2],[2,3],[3,4],[1,3]]
#   Output: 1
#   Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

# Approach:
# Sort the intervals by their finishing time. For each one, check if 
# it overlaps with the previous selected one. If it does, count.
# Greedy algorithm

# Complexity
# O(N*log(N)) time
# O(N) space

def eraseOverlapIntervals(intervals):
	if not intervals or len(intervals) == 1:
		return intervals
	# Sort by finishing time
	sortedIntervals = sorted(intervals, key=lambda x: x[1])
	resp = [sortedIntervals[0]]
	for i in range(1,len(sortedIntervals)):
		if sortedIntervals[i][0] >= resp[-1][1]:
			resp.append(sortedIntervals[i])
	return resp

if __name__ == "__main__":
	print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
	print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
	print(eraseOverlapIntervals([[1,2],[2,3]]))
