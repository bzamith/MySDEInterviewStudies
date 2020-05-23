# Source: Cracking the Coding Interview, 17.19

# Problem: "Missing Two"

# Example:
# Given an array of unique numbers from 1..N, return the two numbers
# that are missing. Do it in O(N) time and O(1) space

# Approach: Compute product and sum of elements, compare to formula
# SUM(1..n) = (n*(n+1))/2
# PROD(1..n) = n!
# x + y = SUM(1..n) - actualSum
# x * y = PROD(1..n) - actualProd

from math import sqrt

def missingTwo(array):
    if not array:
        return None
    n = max(array)
    if n < 3:
        return None
    expectedSum = calculateExpectedSum(n)
    expectedProd = calculateExpectedProd(n)
    actSum, actProd = calculateActualSumProd(array)
    diffSum = expectedSum-actSum
    diffProd = expectedProd/actProd
    delta = (diffSum*diffSum)-(4*diffProd)
    if delta < 0:
        return None
    else:
        y1 = (diffSum + sqrt(delta))/2
        y2 = (diffSum - sqrt(delta))/2
        x1 = diffSum - y1
        x2 = diffSum - y2
        if n <= x1 <= 0 or n <= y1 <= 0:
            return [int(x2),int(y2)]
        else:
            return [int(x1),int(y1)]

def calculateActualSumProd(array):
    actProd = 1
    actSum = 0
    for element in array:
        actProd *= element
        actSum += element
    return actSum, actProd

def calculateExpectedSum(n):
    return (n*(n+1))/2

def calculateExpectedProd(n):
    expectedProd = 1
    for i in range(2,n+1):
        expectedProd *= i
    return expectedProd

if __name__ == '__main__':
    print(missingTwo([1, 4]))
    print(missingTwo([2, 3, 1, 7, 5]))
