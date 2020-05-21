class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        x = 0
        for num in A:
            x ^= num
        
        y = 0
        for num in range(1, len(A)):
            y ^= num
        
        return x^y

class Solution2:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        setted = set(A)
        return sum(A) - sum(setted)

class Solution3:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        if isinstance(A,tuple):
            A=sorted(A)
        else:
            A.sort()
        for i in range(1,len(A)):
            if A[i] == A[i-1]:
                return A[i]
        return -1

class Solution4:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        hashmap = {}
        for element in A:
            if element in hashmap.keys():
                return element
            else:
                hashmap[element] = True