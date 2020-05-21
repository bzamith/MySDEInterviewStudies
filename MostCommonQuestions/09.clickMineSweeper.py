# Source: https://www.udemy.com/course/11-essential-coding-interview-questions/

# Problem: "Find were to expand in a mine sweeper game"

# Example: 
#  [[0,0,0,0,0],
#  [0,1,1,1,0],
#  [0,1,-1,1,0]]
# when clicking [0,1]
#  [[-2,-2,-2,-2,-2],
#  [-2,1,1,1,-2],
#  [-2,1,-1,1,-2]]

# Approach:
# Depth-first or breadth-first searches. However, I don't wanna keep track
# of visited nodes. Since I am changing them to -2, this is a stop condition
# already. Recursion with depth-first

# Complexity:
# O(N*M) time
# O(1) space

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

def click(mineMap, numRows, numCols, givenI, givenJ):
	if mineMap[givenI][givenJ] != 0:
		return mineMap
	else:
		mineMap[givenI][givenJ] = -2
		for i in range(givenI-1, givenI+2):
			for j in range(givenJ-1, givenJ+2):
				if 0 <= i < numRows and 0 <= j < numCols:
					mineMap = click(mineMap, numRows, numCols, i, j)
	return mineMap

if __name__ == "__main__":
	mineMap = mineSweeper([[0,0],[3,3]], 4, 4)
	print(mineMap)
	print("====================================")
	clickedMineMap = click(mineMap, 4, 4, 0, 2)
	print(clickedMineMap)
	print("====================================")
	mineMap = mineSweeper([[2,2]], 3, 5)
	print(mineMap)
	print("====================================")
	clickedMineMap = click(mineMap, 3, 5, 0, 1)
	print(clickedMineMap)