class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        if len(A) == 0:
            raise Exception('Invalid input')
        currSum = 0
        maxSum = A[0]
        for element in A:
            currSum += element
            maxSum = max(maxSum,currSum)
            if currSum < 0:
                currSum = 0
        return maxSum