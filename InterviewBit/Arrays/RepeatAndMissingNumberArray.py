class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        x = sum(A) - sum(set(A))
        k = sum(A) - int(n*(n+1)/2)
    
        return [x,x-k]

class Solution2:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        if len(A) < 2:
            raise Exception('Invalid input')
        A = list(A)
        A.sort()
        result = [0,0]
        for i in range(0, len(A)-1):
            if A[i+1] != A[i]+1:
                if A[i] == A[i+1]:
                    result[0] = A[i]
                else:
                    result[1] = A[i] + 1
        if result[1] == 0:
            if A[0] > 1:
                result[1] = 1
            else:
                result[1] = A[len(A)-1] + 1
        return result
