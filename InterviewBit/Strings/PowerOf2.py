class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        n=int(A)
        if n==1 :
            return 0
        if n & (n-1)==0:
            return 1
        else:
            return 0

class Solution2:
    # @param A : string
    # @return an integer
    def power(self, A):
        A = int(A)
        if A <= 1:
            return 0
        rest = 0
        while rest == 0 and A > 1:
            A = A/2
            rest = A%2
        if A == 1:
            return 1
        else:
            return 0
            
