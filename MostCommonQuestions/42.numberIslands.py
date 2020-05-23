# Source: https://leetcode.com/problems/number-of-islands/submissions/

# Problem: "Number of Islands"

# Example: Given a 2d grid map of '1's (land) and '0's (water), count the number of 
# islands. An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all 
# surrounded by water.

# Approach: BFS or DFS

import queue

def numIslandsDFS(grid):
    if not grid:
        return 0
    dfsStack = queue.LifoQueue()
    nbRows = len(grid)
    nbCols = len(grid[0])
    countIslands = 0
    for row in range(nbRows):
        for col in range(nbCols):
            if grid[row][col] == "1" and (row, col):
                countIslands += 1
                dfsStack.put((row, col))
                while dfsStack.qsize() > 0:
                    currVisiting = dfsStack.get()
                    grid[currVisiting[0]][currVisiting[1]] = 0
                    neighbors = self.getNeighbors(currVisiting, nbRows, nbCols)
                    for neighbor in neighbors:
                        if grid[neighbor[0]][neighbor[1]] == "1":
                            dfsStack.put(neighbor)
    return countIslands

def numIslandsBFS(grid):
    if not grid:
        return 0
    visited = {}
    bfsQueue = queue.Queue()
    nbRows = len(grid)
    nbCols = len(grid[0])
    countIslands = 0
    for row in range(nbRows):
        for col in range(nbCols):
            if grid[row][col] == "1" and (row, col) not in visited:
                countIslands += 1
                bfsQueue.put((row, col))
                while bfsQueue.qsize() > 0:
                    currVisiting = bfsQueue.get()
                    if currVisiting not in visited:
                        visited[currVisiting] = True
                        neighbors = getNeighbors(currVisiting, nbRows, nbCols)
                        for neighbor in neighbors:
                            if grid[neighbor[0]][neighbor[1]] == "1" and neighbor not in visited: 
                                bfsQueue.put(neighbor)
    return countIslands
                
def getNeighbors(point, nbRows, nbCols):
    neighbors = []
    row = point[0]
    col = point[1]
    if row - 1 >= 0:
        neighbors.append((row-1,col))
    if col - 1 >= 0:
        neighbors.append((row,col-1))
    if row + 1 < nbRows:
        neighbors.append((row+1,col))
    if col + 1 < nbCols:
        neighbors.append((row,col+1))
    return neighbors
                
