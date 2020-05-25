# Source: https://leetcode.com/problems/product-of-array-except-self/

# Problem: "Product of Array Except Self"

# Example: Solve it without division and in O(n).

# Approach: If we did not have the constraint of not being able to divide,
#  we would multiply the entire array and keep dividing
#  Since it is not the case, we can multiply left and right of each element

def productExceptSelf(nums):
    if not nums: 
        return None
    if len(nums) == 1:
        return nums[0]
    leftMult = [1 for i in range(len(nums))]
    rightMult = [1 for i in range(len(nums))]
    resp = [0 for i in range(len(nums))]
    currMult = 1
    for i in range(1,len(nums)):
        currMult *= nums[i-1]
        leftMult[i] = currMult
    currMult = 1
    for i in range(len(nums)-2, -1, -1):
        currMult *= nums[i+1]
        rightMult[i] = currMult
    for i in range(0,len(nums)):
        resp[i] = leftMult[i] * rightMult[i]
    return resp

