def minDepth(root):
    if not root:
        return 0
    if None in [root.left, root.right]:
        return max(minDepth(root.left), minDepth(root.right)) + 1
    else:
        return min(minDepth(root.left), minDepth(root.right)) + 1
