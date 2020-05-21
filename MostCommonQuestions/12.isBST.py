# Source: https://www.udemy.com/course/11-essential-coding-interview-questions/

# Problem: "Write a function that takes a binary tree and returns true
# if it is a BST and false if it is not"

# Questions:
# 1. What should I return if null entry?

# Approach:
# Traverse inline and check if the result is a sorted list (Solution 2)
# Use upperLimit and lowerLimit variables

# Complexity:
# O(N) time
# O(log(N)) space (recursion)

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def isBSTBestApproach(node, lowerLim=None, upperLim=None):
    if lowerLim is not None and node.value < lowerLim:
        return False
    if upperLim is not None and upperLim < node.value:
        return False

    isLeftBST = True
    isRightBST = True
    if node.left:
        isLeftBST = isBSTBestApproach(node.left, lowerLim, node.value)
    if isLeftBST and node.right:
        isRightBST = isBSTBestApproach(node.right, node.value, upperLim)
    return isLeftBST and isRightBST

def isBST(node):
    def arrayBSTInLine(node):
        if not node:
            return
        arrayBSTInLine(node.left)
        arrayBST.append(node.value)
        arrayBSTInLine(node.right)

    arrayBST = []
    arrayBSTInLine(node)
    if len(arrayBST) == 1:
        return True
    for i in range(1,len(arrayBST)):
        if arrayBST[i-1] > arrayBST[i]:
            return False
    return True

def create_tree(mapping, head_value):
    head = Node(head_value)
    nodes = {head_value: head}
    for key, value in mapping.items():
        nodes[value[0]] = Node(value[0])
        nodes[value[1]] = Node(value[1])
    for key, value in mapping.items():
        nodes[key].left = nodes[value[0]]
        nodes[key].right = nodes[value[1]]
    return head

if __name__ == "__main__":
    mapping0 = {0: [1, 2]}
    mapping1 = {0: [1, 2], 1: [3, 4], 2: [5, 6]}
    mapping2 = {3: [1, 4], 1: [0, 2], 4: [5, 6]}
    mapping3 = {3: [1, 5], 1: [0, 2], 5: [4, 6]}
    mapping4 = {3: [1, 5], 1: [0, 4]}
    head0 = create_tree(mapping0, 0)
    head1 = create_tree(mapping1, 0)
    head2 = create_tree(mapping2, 3)
    head3 = create_tree(mapping3, 3)
    head4 = create_tree(mapping4, 3)

    print(isBST(head0)) #should return False
    print(isBST(head1)) #should return False
    print(isBST(head2)) #should return False
    print(isBST(head3)) #should return True
    print(isBST(head4)) #should return False