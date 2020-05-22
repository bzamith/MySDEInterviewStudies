# Source: https://www.youtube.com/watch?v=bGC2fNALbNU

# Problem: "All Subsets of a Set"

# Example: 
#  Given a set of distinct integers, nums, return all possible subsets (the power set).
#  [1,2,3] -> [[3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[]]

# Approach:
# Let's start from empty subset in output list. At each step one takes new integer into 
# consideration and generates new subsets from the existing ones.

# Complexity:
# O(N*(2^N)) time
# O(N*(2^N)) space

def subsets(nums):
    resp = [[]]
    for num in nums:
        curr = []
        for prev in resp:
            curr += [prev + [num]]
        resp += curr
    return resp

if __name__ == "__main__":
    print(subsets([0,1,2,3]))
    print(subsets([1,5,9,2]))