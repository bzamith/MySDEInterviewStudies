# Source: https://www.youtube.com/watch?v=qli-JCrSwuk&t=196s

# Problem: "How Many Ways to Decode This Message?"

# Example: 
#  Let 1 represent ‘A’, 2 represents ‘B’, etc. Given a digit sequence, 
#  count the number of possible decodings of the given digit sequence. 
#  "121" -> 3 ("ABA", "AU", "LA")

# Brute-force solution:
# Recursion. num_ways("12345") = num_ways("2345") + num_ways("345")

# Approach:
# Use Dynamic Programming to avoid recalculating the same stuff
# Base cases: num_ways("011") = 0
#             num_ways("2734") = num_ways("7345")

# Complexity:
# O(N) time
# O(N) space

def numDecodingsBestApproach(digits):
    memo = [None for i in range(len(digits)+1)]
    def numDecodingsHelper(digits, n): 
        if n == 0:  
            return 1
        s = len(digits) - n
        if digits[s] == "0":  
            return 0
        if memo[n] != None:
            return memo[n]
        result = numDecodingsHelper(digits, n-1)
        if n >= 2 and int(digits[s:s+2]) <= 26:
            result += numDecodingsHelper(digits, n - 2)  
        memo[n] = result
        return result  
    return numDecodingsHelper(digits,len(digits))  

def numDecodings(digits):
    def numDecodingsHelper(digits, n):  
        if n == 0:  
            return 1
        s = len(digits) - n
        if digits[s] == "0":  
            return 0
        result = numDecodingsHelper(digits, n-1)
        if n >= 2 and int(digits[s:s+2]) <= 26:
            result += numDecodingsHelper(digits, n - 2)  
        return result  
    return numDecodingsHelper(digits,len(digits));  

if __name__ == "__main__":
    print(numDecodingsBestApproach("1256"))
    print(numDecodings("1256"))
    print(numDecodings("121043"))