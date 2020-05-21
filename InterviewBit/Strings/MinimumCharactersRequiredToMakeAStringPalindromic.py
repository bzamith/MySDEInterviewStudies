class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        if len(A) <= 1:
            return 0
        i, j, j_start = 0, len(A)-1, len(A)-1
        while i < j:
            if A[i] == A[j]:
                i += 1
                j -= 1
            else:
                j = j_start - 1
                j_start = j
                i = 0
        return len(A) - 1 - j_start

class Solution2:
    # @param A : string
    # @return an integer
    
    def is_palindrome(self,A):
        if(len(A) == 1):
            return 1
        N = len(A)
        for i in range(0,int(N/2)):
            if(A[i] != A[N-i-1]):
                return 0
        return 1
    
    
    def solve(self, A):
        if(len(A) == 0):
            return 0
        j = len(A)-1
        while(j >= 0):
            if(self.is_palindrome(A[0:j+1]) == 1):
                return len(A)-j-1
            j -= 1
