# Source: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Problem: "Remove Duplicates from Sorted Array in Place"

# Example: 
#  Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
#  Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Approach:
# Two-pointers approach

# Complexity:
# O(N) time
# O(1) space

def removeDuplicates(nums):
    count = 0
    if len(nums) < 2:
    	return nums
    for i in range(1,len(nums)):
        if nums[i] == nums[i-1]:
            count += 1
        else:
            nums[i-count] = nums[i]
    return nums[0:len(nums) - count]

if __name__ == "__main__":
    print(removeDuplicates([0,0,0,1,1,2,3]))
    print(removeDuplicates([0,0,1,2,3,3]))
    