class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        res = [[0 for i in range(A)] for j in range(A)]
        rowBegin = 0
        rowEnd = A - 1
        colBegin = 0
        colEnd = A - 1
        count = 1
        
        while rowBegin <= rowEnd and colBegin <= colEnd:
            for i in range(colBegin, colEnd + 1):
                res[rowBegin][i] = count
                count += 1
            rowBegin += 1
                
            for i in range(rowBegin, rowEnd + 1):
                res[i][colEnd] = count
                count += 1
            colEnd -= 1
            
            if rowBegin <= rowEnd:
                for i in range(colEnd, colBegin-1, -1):
                    res[rowEnd][i] = count
                    count += 1
            rowEnd -= 1
                
            if colBegin <= colEnd:
                for i in range(rowEnd, rowBegin-1, -1):
                    res[i][colBegin] = count
                    count += 1
            colBegin += 1
        
        return res
            
            