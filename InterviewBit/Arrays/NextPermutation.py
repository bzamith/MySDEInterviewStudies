class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextPermutation(self, A):
        if len(A) < 2:
            return A
        if len(A) == 2:
            swap = A[0]
            A[0] = A[1];
            A[1] = swap
            return A
        i = self.findSufixIndex(A)
        if i <= 0:
            return A
        j = self.findRightMostHigherPivotIndex(A, i)
        swap = A[i - 1]
        A[i - 1] = A[j];
        A[j] = swap
        A = self.reverseSufix(A,i)
        return A
    
    def findSufixIndex(self, A):
        i = len(A) - 1
        while i >= 0 and A[i-1] >= A[i]:
            i -= 1
        return i
    
    def findRightMostHigherPivotIndex(self, A, i):
        j = len(A) -1
        while A[j] <= A[i-1]:
            j -= 1
        return j
        
    def reverseSufix(self, A, i):
        j = len(A) - 1
        while i < j:
            swap = A[i]
            A[i] = A[j]
            A[j] = swap
            i+=1
            j-=1
        return A
        