class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        res = self.getNumber(A[-1])
        for i in range(1, len(A)):
            res += pow(26,i)*self.getNumber(A[-i-1])
        return res

    def getNumber(self, A):
        return ord(A) - 64