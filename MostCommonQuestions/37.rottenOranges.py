# Source: https://leetcode.com/problems/rotting-oranges/

# Problem: "Rotting Oranges"

# Example:
# In a given grid, each cell can have one of three values:
#    the value 0 representing an empty cell;
#    the value 1 representing a fresh orange;
#    the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (4-directionally) 
# to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no 
# cell has a fresh orange.  If this is impossible, return -1 instead.

# Approach:
# BFS. Don't have to keep track of visited because it is turning 2

import queue

class Solution:
    def orangesRotting(self, grid):
        toVisit = queue.Queue()
        nbRow = len(grid)
        nbCol = len(grid[0])
        countFresh = 0
        for row in range(0, nbRow):
            for col in range(0, nbCol):
                if grid[row][col] == 2:
                    toVisit.put((row,col))
                elif grid[row][col] == 1:
                    countFresh += 1
        countRotten = toVisit.qsize()
        if countFresh ==  0:
            return 0
        if countRotten == 0:
            return -1
        countMin = 0
        while countRotten > 0:
            #print("==========")
            #print(countMin)
            for i in range(countRotten):
                curr = toVisit.get()
                neighbors = self.getNeighbors(curr[0],curr[1],nbRow,nbCol)
                for neighbor in neighbors:
                    if grid[neighbor[0]][neighbor[1]] == 1:
                        #print(neighbor, end=",")
                        toVisit.put(neighbor)
                        grid[neighbor[0]][neighbor[1]] = 2
                        countFresh -= 1
                #print()
            countRotten = toVisit.qsize()
            countMin += 1
        return countMin-1
                    
    def getNeighbors(self, row, col, nbRow, nbCol):
        neighbors = []
        if row - 1 >= 0:
            neighbors.append((row-1,col))
        if col - 1 >= 0:
            neighbors.append((row,col-1))
        if row + 1 < nbRow:
            neighbors.append((row+1,col))
        if col + 1 < nbCol:
            neighbors.append((row,col+1))
        return neighbors

if __name__ == '__main__':
    sol = Solution()
    print(sol.orangesRotting([[1,2]]))
