class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
	    max1 = -2147483648
	    min1 = +2147483647
	    max2 = -2147483648
	    min2 = +2147483647
    	for i in range(len(A)):  
	        max1 = max(max1, A[i] + i) 
	        min1 = min(min1, A[i] + i) 
	        max2 = max(max2, A[i] - i) 
	        min2 = min(min2, A[i] - i)  
    	return max(max1 - min1, max2 - min2) 

class Solution2:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        maxF = 0
        for i in range(0,len(A)-1):
            for j in range(i+1, len(A)):
                maxF = max(maxF, self.f(A,i,j)) 
        return maxF
        
    def f(self, A, i, j):
        return abs(A[i] - A[j]) + abs(i- j)

class Solution3:
    def maxArr(self, A):
        dict = {}
        maxF = 0
        for i in range(0,len(A)-1):
            for j in range(i+1, len(A)):
                key = str(i)+','+str(j)
                if key not in dict:
                    fValue = self.f(A,i,j)
                    dict[key] = fValue
                    maxF = max(maxF, fValue) 
        return maxF
        
    def f(self, A, i, j):
        return abs(A[i] - A[j]) + abs(i- j)