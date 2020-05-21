class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        if A <= 1:
            return 1
        if A == 2:
            return 11
        res = str(11)
        for i in range(2, A):
            res = self.count(res)
        return int(res)
                    
    def count(self, nb):
        counter = 1
        res = ''
        for i in range(len(nb)-1):
            if nb[i] == nb[i+1]:
                counter += 1
            else:
                res += str(counter) + nb[i]
                counter = 1
        res += str(counter) + nb[-1]
        return res
