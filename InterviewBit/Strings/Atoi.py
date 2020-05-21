class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        nb = self.getNumber(A)
        res = 0
        for i in range(len(nb)-1,-1,-1):
            res += (ord(nb[i]) - 48) * pow(10,len(nb)-1-i)
        return res
        
    def getNumber(self, A):
        i = 0
        nb = ''
        while A[i] == ' ' and i < len(A) - 1:
            i += 1
        while ord(A[i]) > 47 and ord(A[i]) < 58 and i < len(A) - 1:
            nb += A[i]
            i += 1
        return nb

class Solution2:
    # @param A : string
    # @return an integer
    def atoi(self, A: str):
        # Define max and min values
        max_int = 2147483647
        min_int = -max_int - 1

        # Remove any trailing spaces
        A = A.strip()

        # Check if a sign of the number is written
        is_sign_specified = A[0] == '-' or A[0] == '+'

        # Try reading a number
        is_negative = A[0] == '-'

        # Whatever has to be parsed into a number
        num_str = ''
        
        # Starting index
        i = 1 if is_sign_specified else 0
        while i < len(A) and A[i] in '1234567890':
            num_str += A[i]

            i += 1

        # If no number was read
        if len(num_str) == 0:
            return 0

        ans = int(num_str) * (-1 if is_negative else 1)

        if ans > max_int:
            ans = max_int

        if ans < min_int:
            ans = min_int
        return ans

