class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        if A == 0:
            return []
        sol = [[1]]
        for i in range(1,A):
            res = self.generateRow(sol[-1])
            sol.append(res)
        return sol

    def generateRow(self, lastRow):
        res = [0 for i in range(len(lastRow)+1)]
        res[0] = lastRow[0]
        res[-1] = lastRow[-1]
        for i in range(1,len(lastRow)):
            res[i] = lastRow[i] + lastRow[i-1]
        return res