class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        if len(B) > len(A):
            return -1
        if A == '' or B == '':
            return -1
        for i in range(len(A)):
            if A[i] == B[0]:
                if A[i:i+len(B)] == B:
                    return i
        return -1
            
class Solution2:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        try:
            return A.index(B)
        except:
            return -1

