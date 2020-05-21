# Source: https://www.youtube.com/watch?v=xG6In1ISnB0

# Problem: "Calculate Fibonacci Series"

# Example: 
#  F(n) = F(n-1) + F(n-2)
#  F(9) = 34

# Brute-force solution:
# Use recursion: O(2^N) time and O(N) space (stack size)

# Approach:
# Dynamic Programming to store already calculated solutions (Solution 2).
# Optimize even more by keeping the previous 2 results and iterating
# (Solution 1).

# Complexity:
# O(N) time
# O(1) space

def fibonacciBestApproach(n): 
    a = 0
    b = 1
    if n < 0: 
        return None
    elif n < 2: 
        return n
    else: 
        for i in range(2,n+1): 
            c = a + b 
            a = b 
            b = c 
        return b 

def fibonacci(n):  
    FibArray = [0, 1]
    while len(FibArray) < n + 1:  
        FibArray.append(0) 
    if n <= 1:  
        return n  
    else:  
        if FibArray[n - 1] == 0:  
            FibArray[n - 1] = fibonacci(n - 1)
        if FibArray[n - 2] == 0:  
            FibArray[n - 2] = fibonacci(n - 2)   
    FibArray[n] = FibArray[n - 2] + FibArray[n - 1]  
    return FibArray[n]

if __name__ == "__main__":
	print(fibonacciBestApproach(9))
	print(fibonacci(9))
