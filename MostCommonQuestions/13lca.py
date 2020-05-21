# Source: https://www.udemy.com/course/11-essential-coding-interview-questions/

# Problem: "Find the lowest common ancestor of a binary tree"

# Questions:
# 1. Is it a BST? No
# 2. Are there duplicates? No

# Approach:
# Store paths (Solution 1)
# Single traversal + recursion (Solution 2)

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def lcaBestApproach(root, j, k):
    if root is None:
        return None
    if root.value == j or root.value == k:
        return root
    leftLca = lca(root.left, j, k)
    rightLca = lca(root.right, j, k)
    if leftLca and rightLca:
        return root
    if leftLca:
        return leftLca
    else:
        return rightLca

def lca(root, j, k):
    pathToJ = pathToX(root, j)
    pathToK = pathToX(root, k)
    resp = None
    while pathToJ and pathToK:
        jPop = pathToJ.pop()
        kPop = pathToK.pop()
        if jPop is kPop:
            resp = jPop
        else:
            break
    return resp

def pathToX(root, x):
    if root is None:
        return None
    if root.value == x:
        return [root]
    leftPath = pathToX(root.left, x)
    if leftPath:
        leftPath.append(root)
        return leftPath
    rightPath = pathToX(root.right, x)
    if rightPath:
        rightPath.append(root)
        return rightPath
    return None