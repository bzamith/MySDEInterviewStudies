class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        totalDist = 0
        if len(A) != len(B):
            raise Exception('Invalid input')
        for i in range(0,len(A)-1):
            totalDist += self.distPoints(A[i],B[i],A[i+1],B[i+1])
        return totalDist
        
    def distPoints(self, x0, y0, x1, y1):
        xMovs = abs(x0-x1)
        yMovs = abs(y0-y1)
        return max(xMovs,yMovs)