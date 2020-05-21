class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        for i in range(len(A)):
            if A[i] == B:
                return i
        return -1

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        pivot = self.pivotSearch(A,B)
        idx1 = self.binarySearch(A, B, 0, pivot)
        idx2 = self.binarySearch(A, B, pivot)
        return max(idx1, idx2)

    def binarySearch(self, A, B, low = None, high = None):
        n = len(A)-1
        if not low:
            low = 0
        if not high:
            high = n
        
        while low <= high:
            mid = (low+high)//2
            if A[mid] == B:
                return mid
            elif A[mid] > B:
                high = mid-1
            else:
                low = mid+1
        return -1

    def pivotSearch(self, A, B):
        n = len(A)-1
        low, high = 0, n
        
        while low <= high:
            mid = (low+high)//2
            if A[mid-1] > A[mid] and A[mid] < A[mid+1]:
                return mid
            elif A[low] < A[mid]:
                low = mid+1
            else:
                high = mid-1
        return 0