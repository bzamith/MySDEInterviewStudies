# Source: https://www.udemy.com/course/11-essential-coding-interview-questions/

# Problem: "Assign numbers in a mine sweeper game"

# Example: 
#  mineSweeper(bombs, numRows, numCols)
#  mineSweeper([[0,0],[0,1]],3,4)
#  [[-1.-1.1.0],
#  [2,2,1,0],
#  [0,0,0,0]]

# Questions:
# 1. How are bombs represented? -1
# 2. Are there duplicates in bombs? No

# Brute-force solution:
# Iterate over the entire matrix (O(N^2))

# Approach:
# When inserting a bomb, update the surroundings

def mineSweeper(bombs, numRows, numCols):
	mineMap = [[0 for i in range(numCols)] for j in range(numRows)]
	if not bombs:
		return mineMap
	for bomb in bombs:
		i = bomb[0]
		j = bomb[1]
		mineMap[i][j] = -1
		for iNeighbor in range(i-1,i+2):
			for jNeighbor in range(j-1, j+2):
				if 0 <= iNeighbor < numRows and 0 <= jNeighbor < numCols and mineMap[iNeighbor][jNeighbor] != -1:
					mineMap[iNeighbor][jNeighbor] += 1
	return mineMap

if __name__ == "__main__":
	print(mineSweeper([[0,0],[0,1]],3,4))