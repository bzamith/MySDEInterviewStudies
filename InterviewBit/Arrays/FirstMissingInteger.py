class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        maxN = max(A)
        if maxN <= 0:
            return 1
        auxArray = [0 for i in range(maxN)]
        for element in A:
            if element > 0:
                auxArray[element-1] = 1
        for i in range(maxN):
            if auxArray[i] == 0:
                return i+1
        return maxN + 1

class Solution2:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        lenA = len(A)
        A.sort()
        i = 0
        while i < lenA and A[i] <= 0:
            i+=1
        if i == lenA or A[i] > 1:
            return 1
        while i < lenA - 1 and A[i] == A[i+1] - 1:
            i+=1
        return A[i] + 1