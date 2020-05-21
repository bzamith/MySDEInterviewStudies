from math import factorial
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    # (A-1) steps down, (B-1) steps right, (A+B-2) steps in total
    # Combinatorial analysis: (A+B-2)!/((A-1)!(B-1)!)
    def uniquePaths(self, A, B):
        return factorial(A+B-2)//factorial(A-1)//factorial(B-1)

class Solution2:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        matrix = [[0 for i in range(B)] for j in range(A)]
        matrix[0][0] = 1
        for i in range(A):
            for j in range(B):
                if i >= 1:
                    matrix[i][j] += matrix[i-1][j]
                if j >= 1:
                    matrix[i][j] += matrix[i][j-1]
        return matrix[A-1][B-1]
