# Source: https://www.youtube.com/watch?v=jJPtLzq1E-Y&t=24s
# Source: https://www.youtube.com/watch?v=wGbuCyNpxIg

# Problem: "N-Queens Problem"

# Example: 
#   The n-queens puzzle is the problem of placing n queens on an n×n 
#   chessboard such that no two queens attack each other.
#   A queen can move horizontally, vertically and diagonally.

# Approach:
# Backtracking
# Go column by column
# 2. Check if in same row
# 3. Check if in diagonal -> abs(deltaX/deltaY) == 1
# It would be more optimal to use linked-lists instead of
# arrays of arrays, become we are backtracking

# Backtracking
# 1. Our choice
#   - What choice do we make at each call of the function?
#   - Recursion represents a decision
# 2. Our constraints
#   - When do we stop following a certain path?
#   - When do we not even go a certain way?
# 3. Our Goal
#   - What's our target?
#   - What are we trying to find?
#   - Base case comes from this

# Complexity:
# O(N) time
# O(N) space (recursion)

def nQueens(n):
	def isValid(colPlacements):
		rowId = len(colPlacements)-1
		for i in range(0,rowId):
			diff = abs(colPlacements[i]-colPlacements[rowId])
			if diff == 0 or diff == rowId - i:
				return False
		return True

	def solveNQueens(n, row, colPlacements):
		# 3. Our Goal
		if row == n:
			result.append(colPlacements.copy())
		else:
			for col in range(0,n):
				# 1. Our Choice
				colPlacements.append(col)
				# 2. Our constraints
				if isValid(colPlacements):
					solveNQueens(n, row+1, colPlacements)
				# Undo our choice
				colPlacements.pop()

	result = []
	solveNQueens(n,0,[])
	return result

if __name__ == "__main__":
	print(nQueens(4))
	

