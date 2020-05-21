class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        lenA = len(A)
        if lenA <= 1:
            return 1
        slot = 1
        curr = A[0]
        for i in range(1,lenA):
            if A[i] != curr:
                curr = A[i]
                A[slot] = A[i]
                slot += 1
        A = A[0:slot]
        return slot