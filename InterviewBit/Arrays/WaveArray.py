class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        lenA = len(A)
        if lenA <= 1:
            return A
        res = sorted(A)
        maxIt = lenA if lenA%2 == 0 else lenA-1
        for i in range(0,maxIt,2):
            swap = res[i]
            res[i] = res[i+1]
            res[i+1] = swap
        return res