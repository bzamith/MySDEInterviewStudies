class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        words = A.split(' ')
        lenWords = len(words)
        if lenWords <= 1:
            return A
        left = 0
        right = lenWords - 1
        while left < right:
            temp = words[left]
            words[left] = words[right]
            words[right] = temp
            left += 1
            right -=1
        return ' '.join(words)

class Solution2:
    # @param A : string
    # @return a strings
    def solve(self, A):
        rev = A.split()
        rev.reverse()
        s = ' '
        s = s.join(rev)
        return s

