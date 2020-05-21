class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        splitedA = list(A.split('.'))
        splitedB = list(B.split('.'))
        for i in range(min(len(splitedA),len(splitedB))):
            if int(splitedA[i]) > int(splitedB[i]):
                return 1
            if int(splitedA[i]) < int(splitedB[i]):
                return -1
        while splitedA[-1] == '0':
            del splitedA[-1]
        while splitedB[-1] == '0':
            del splitedB[-1]
        if len(splitedA) > len(splitedB):
            return 1
        if len(splitedB) > len(splitedA):
            return -1
        else:
            return 0