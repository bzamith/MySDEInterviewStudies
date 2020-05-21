class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
	    if A== 1 : 
	        return True
	    for i in range(2, int(sqrt(A)) + 1) : 
	        val = log(A) / log(i) 
	        if (round((val - int(val)),8) < 0.00000001): 
	            return True
	    return False

class Solution2:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        for i in range(1,A):
            for j in range(1,A):
                if pow(i,j) == A:
                    return True
        return False

class Solution3:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        count = 0
        for i in range(A-1,1,-1):
            rest = A
            while rest > 1 and rest%i == 0:
                count += 1
                rest = rest/i
            if rest == 1:
                return True
        return False