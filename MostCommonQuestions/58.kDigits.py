# Source: https://leetcode.com/problems/remove-k-digits/

# Problem: "Remove K Digits"

# Example: "Given a non-negative integer num represented as a string, 
# remove k digits from the number so that the new number is the smallest 
# possible". 
# "1432219", k = 3 -> "1219"

def removeKdigits(self, num: str, k: int) -> str:    
    stack = []
    for digit in num:
        while k > 0 and len(stack) > 0 and stack[-1] > digit:
            k -= 1
            stack.pop()  
        stack.append(digit)
    if k > 0:
        stack = stack[:-k]     
    return "".join(stack).lstrip("0") or "0"