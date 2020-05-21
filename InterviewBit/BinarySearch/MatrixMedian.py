from bisect import bisect_right
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def binSearch(self, matrix, min_el, max_el, cntElBeforeMed):
        start = min_el
        end = max_el
        while start < end:
            mid = start + ((end - start) // 2)
            cnt = 0
            for row in matrix:
                cnt += bisect_right(row, mid)
            if cnt > cntElBeforeMed:
                end = mid
            else:
                start = mid + 1
        
        return start
    
    def getMinMax(self, matrix):
        min_el = float('inf')
        max_el = float('-inf')
        for row in matrix:
            if min_el > row[0]:
                min_el = row[0]
            if max_el < row[-1]:
                max_el = row[-1]
        
        return min_el, max_el
    
    def findMedian(self, A):
        matrix = A
        rn = len(matrix)
        cn = len(matrix[0])
        cntElBeforeMed = (rn * cn) // 2
        min_el, max_el = self.getMinMax(matrix)
        return self.binSearch(matrix, min_el, max_el, cntElBeforeMed)

class Solution2:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        nbRows = len(A)
        nbCols = len(A[0])
        if nbRows == 0:
            return 0
        if nbRows == nbCols == 1:
            return A[0][0]
        linearMatrix = A[0]
        for i in range(1, nbRows):
            linearMatrix += A[i]
        linearMatrix.sort()
        lenLinearMatrix = len(linearMatrix)
        if lenLinearMatrix%2 == 0:
            median = (linearMatrix[lenLinearMatrix/2-1] + linearMatrix[lenLinearMatrix/2])/2
        else:
            median = linearMatrix[lenLinearMatrix//2]
        return median