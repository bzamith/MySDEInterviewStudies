class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        n = len(A)
        ASorted = sorted(A) 
        start,end=-1,-1
        for i in range(n):
            A[i] = A[i] - ASorted[i]
        for i in range(n-1):
            if(A[0]!=0):
                start=0
                break
            if(A[i]==0 and A[i+1]!=0):
                start = i+1
                break
        for i in range(n-1,0,-1):
            if(A[n-1]!=0):
                end = n-1
                break
            if(A[i]==0 and A[i-1]!=0):
                end = i-1
                break
        if(start==-1 and end==-1):
            return [-1]
        return [start, end]
