# Source: https://www.udemy.com/course/11-essential-coding-interview-questions/

# Problem: "Rotate a 2D array 90 degrees."

# Example: 
#  [[1,2,3],
#  [4,5,6],
#  [7,8,9]]
# becomes
#  [[7,4,1],
#  [8,5,2],
#  [9,6,3]]

# Questions:
# 1. Is it a quadratic matrix? Yes

# Brute-force solution:
# Create new array. resp[j][n-1-i] = givenArray[i][j]. O(N^2) time and space
# But we can find a in-place solution

# Approach:
# Get the sub-rectangles that need to be rotated

# Complexity:
# O(N^2) time
# O(1) space

import math

def rotateBestApproach(givenArray, n):
	for i in range(math.ceil(n/2)):
		for j in range(math.floor(n/2)):
			aux = [-1]*4
			(currI,currJ) = (i,j)
			for k in range(4):
				aux[k] = givenArray[currI][currJ]
				(currI,currJ) = (currJ,n-1-currI)
			for k in range(4):
				givenArray[currI][currJ] = aux[(k-1)%4]
				(currI,currJ) = (currJ,n-1-currI)
	return givenArray

def rotate(givenArray, n):
	resp = [[0 for i in range(n)] for i in range(n)]
	for i in range(n):
		for j in range(n):
			resp[j][n-1-i] = givenArray[i][j]
	return resp

if __name__ == "__main__":
	array = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
	print(rotateBestApproach(array,5))