def pacificAtlantic(matrix):
	def dfs(matrix, row, col, prevVal, ocean):
		# 1. Check necessary conditions
		if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
			return
		if matrix[row][col] < prevVal:
			return
		if ocean[row][col] == 1:
			return

		# 2. Process Cell
		ocean[row][col] = 1

		# 3. Call DFS as needed
		dfs(matrix, row - 1, col, matrix[row][col], ocean)
		dfs(matrix, row + 1, col, matrix[row][col], ocean)
		dfs(matrix, row, col - 1, matrix[row][col], ocean)
		dfs(matrix, row, col + 1, matrix[row][col], ocean)

	if not matrix or len(matrix) == 0:
		return []

	pacific = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
	atlantic = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]

	# top and bottom
	for col in range(0, len(matrix[0])):
		dfs(matrix, 0, col, -1000, pacific)
		dfs(matrix, len(matrix)-1, col, -1000, atlantic)

	# left and right
	for row in range(0, len(matrix[0])):
		dfs(matrix, row, 0, -1000, pacific)
		dfs(matrix, row,  len(matrix[0])-1, -1000, atlantic)

	resp = []

	for row in range(0, len(matrix)):
		for col in range(0, len(matrix[0])):
			if pacific[row][col] == 1 and atlantic[row][col]:
				resp.append([row,col])

	return resp