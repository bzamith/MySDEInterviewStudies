class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        myDict = 'ZABCDEFGHIJKLMNOPQRSTUVWXY'
        sol = ''
        while A > 0:
            aux = A%26
            sol = myDict[aux] + sol
            A = A/26
            if aux == 0:
                A -= 1
        return sol