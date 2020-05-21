class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        for i in range(len(A)-1, -1, -1):
            if A[i] != 9:
                A[i] += 1
                while A[0] == 0:
                    del A[0]
                return A
            else:
                A[i] = 0
        return [1] + A