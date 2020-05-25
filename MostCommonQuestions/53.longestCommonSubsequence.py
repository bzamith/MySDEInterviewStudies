# Source: https://www.youtube.com/watch?v=ASoaQq66foQ
# Source: https://leetcode.com/problems/longest-common-subsequence/

# Problem: "Longest Common Subsequence"

# Example: Given two strings text1 and text2, return the length of their longest common subsequence.
#   A subsequence of a string is a new string generated from the original string with some characters
#   (can be none) deleted without changing the relative order of the remaining characters. 
#   (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is
#   a subsequence that is common to both strings.
#   If there is no common subsequence, return 0.

# Approach: Dynamic Programming

def longestCommonSubsequence(string1, string2, n1, n2):
    if n1 == 0 or n2 == 0:
        return 0
    else:
        if memoize[n1][n2] != None:
            return memoize[n1][n2]
            
        if string1[n1 - 1] == string2[n2 - 1]:
            memoize[n1][n2] = 1 + longestCommonSubsequence(string1, string2, n1 - 1, n2 - 1)
        else:
            memoize[n1][n2] = max(longestCommonSubsequence(string1, string2, n1, n2 - 1), longestCommonSubsequence(string1, string2, n1 - 1, n2))

        return memoize[n1][n2]