class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        lenA = len(A)
        if lenA < 1:
            return 0
        foundFirstLetter = False
        nbLastWord = 0
        nbSpacesBegin = 0
        for i in range(lenA-1, -1, -1):
            if A[i] == ' ' and not foundFirstLetter:
                nbSpacesBegin += 1
            if A[i] != ' ' and not foundFirstLetter:
                foundFirstLetter = True
            if A[i] == ' ' and foundFirstLetter:
                return nbLastWord
            if foundFirstLetter:
                nbLastWord += 1
        return lenA - nbSpacesBegin

class Solution2:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        cnt = 0
        if len(A)==0:
            return cnt
        end = len(A)-1
        while end>=0 and not('0' <= A[end] <= '9' or 'A'<= A[end] <='Z' or 'a' <= A[end] <= 'z') :
            end -= 1
        while end>=0 and ('0' <= A[end] <= '9' or 'A'<= A[end] <='Z' or 'a' <= A[end] <= 'z'):
            cnt += 1
            end -= 1
        return cnt
