# Source: https://leetcode.com/problems/diameter-of-binary-tree/

# Problem: "Diameter of Binary Tree"

# Example: 
#   Given a binary tree, you need to compute the length of the diameter of the tree. 
#   The diameter of a binary tree is the length of the longest path between any two 
#   nodes in a tree. This path may or may not pass through the root. 

# Approach:
# Any path can be written as two arrows (in different directions) from some node, 
# where an arrow is a path that starts at some node and only travels down to child nodes.
# If we knew the maximum length arrows L, R for each child, then the best path touches L + R + 1 nodes.

# Complexity:
# O(N) time
# O(N) space (recursion)

class Solution():
    def diameterOfBinaryTree(self, root):
        self.resp = 0
        def depth(node):
            if not node: 
                return 0
            L = depth(node.left)
            R = depth(node.right)
            self.resp = max(self.resp, L+R)
            return max(L, R) + 1
        depth(root)
        return self.resp    