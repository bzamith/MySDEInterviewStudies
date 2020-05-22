# Source: https://leetcode.com/problems/palindrome-number/

# Problem: "Palindrome Number"

# Example: 
#  Determine whether an integer is a palindrome. 
#  An integer is a palindrome when it reads the same backward as forward.

# Approach:
# Create an array with the digits. Two-pointers approach (Solution 1)
# Reverse the array and compare (Solution 2)

# Complexity:
# O(N) time
# O(N) space

def isPalindromeBestApproach(number):
    if x < 0:
        return False
    number = str(abs(x))
    left = 0
    right = len(hList)-1
    while left < right:
        if hList[left] != hList[right]:
            return False
        left += 1
        right -= 1
    return True

def isPalindrome(number):
    if x < 0:
        return False
    number = str(abs(x))
    numberReversed = str(x)[::-1]
    return number == numberReversed

def numberToArray(number):
    hList = []
    while number > 0:
        hList.append(number%10)
        number = number//10
    return hList

if __name__ == "__main__":
    print(isPalindromeBestApproach(12341))
    print(isPalindromeBestApproach(1234321))