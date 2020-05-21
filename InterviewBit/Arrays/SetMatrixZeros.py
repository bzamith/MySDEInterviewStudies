class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        nbRows = len(A)
        nbCols = len(A[0])
        firstRow = False
        firstCol = False
        for j in range(nbCols):
            if A[0][j] == 0:
                firstRow = True
        
        for i in range(nbRows):
            if A[i][0] == 0:
                firstCol = True
        
        for i in range(nbRows):
            for j in range(nbCols):
                if A[i][j] == 0:
                    A[i][0] = 0
                    A[0][j] = 0
    
        for i in range(nbRows):
            for j in range(nbCols):
                if A[0][j] == 0 or A[i][0] == 0:
                    A[i][j] = 0
    
        if firstRow == True:
            for i in range(nbCols):
                A[0][i] = 0
    
        if firstCol == True:
            for i in range(nbRows):
                A[i][0] = 0
        return A

class Solution2:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        nbRows = len(A)
        nbCols = len(A[0])
        arrayCols = [False for i in range(nbCols)]
        for i in range(nbRows):
            for j in range(nbCols):
                if A[i][j] == 0:
                    arrayCols[j] = True
        for i in range(nbRows):
            containsZero = False
            for j in range(nbCols):
                if A[i][j] == 0:
                    containsZero = True
                    break
            for j in range(nbCols):
                if containsZero or arrayCols[j]:
                    A[i][j] = 0
        return A

class Solution3:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        rows = set()
        cols = set()
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]==0:
                    rows.add(i)
                    cols.add(j)
        for i in rows:
            for j in range(len(A[0])):
                A[i][j] = 0
        for j in cols:
            for i in range(len(A)):
                A[i][j] = 0
        return A

class Solution4:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        nbRows = len(A)
        nbCols = len(A[0])
        hashRows = {}
        hashCols = {}
        for i in range(nbRows):
            for j in range(nbCols):
                if A[i][j] == 0:
                    hashRows[i] = True
                    hashCols[j] = True
        for i in hashRows.keys():
            for j in range(len(A[0])):
                A[i][j] = 0
        for j in hashCols.keys():
            for i in range(len(A)):
                A[i][j] = 0
        return A
        