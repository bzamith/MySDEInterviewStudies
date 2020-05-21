class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        array = list(range(len(A)))
        array.sort(key = lambda i: A[i])
        maxDistance = 0
        minSofar = array[0]
        for i in array:
            if i <= minSofar:
                minSofar = i
            else:
                maxDistance = max(maxDistance,i - minSofar)
        return maxDistance

class Solution2:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        lenA = len(A)
        maxDist = 0
        for i in range(lenA):
            j = lenA - 1
            while not self.constraint(A, i, j) and (j-i) > maxDist:
                j -= 1
            maxDist = max(maxDist, j-i)
        return maxDist
                
    def constraint(self, A, i, j):
        return A[i] <= A[j]