class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        slot = 0
        for x in A:
            if x != B:
                A[slot] = x
                slot += 1
        return slot

class Solution2:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        i = 0
        while i < len(A):
            if A[i] == B:
                del A[i]
            else:
                i += 1
        return len(A)