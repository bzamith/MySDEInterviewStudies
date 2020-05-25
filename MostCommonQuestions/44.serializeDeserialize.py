# Source: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Problem: "Serialize and Deserialize Binary Tree"

# Approach: DFS ou BFS

import queue

class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class CodecDFS:
    def serialize(self, root):
        if not root:
            return "X,"
        leftSerialized = self.serialize(root.left)
        rightSerialized = self.serialize(root.right)
        return str(root.val) + "," + str(leftSerialized) + str(rightSerialized) 

    def deserialize(self, data):
        nodesLeft = queue.Queue()
        nodes = data.split(',')
        for node in nodes:
            nodesLeft.put(node)
        return self.deserializeHelper(nodesLeft)
    
    def deserializeHelper(self, nodesLeft):
        valueForNode = nodesLeft.get()
        if valueForNode == "X":
            return None
        newNode = TreeNode(valueForNode)
        newNode.left = self.deserializeHelper(nodesLeft)
        newNode.right = self.deserializeHelper(nodesLeft)
        return newNode

class CodecBFS:
    def serialize(self, root):
        if not root:
            return None
        
        bfsQueue = queue.Queue()
        bfsQueue.put(root)
        resp = [str(root.val)]
        
        while bfsQueue.qsize() > 0:
            curr = bfsQueue.get()
            if curr.left is None:
                resp.append("X")
            else:
                bfsQueue.put(curr.left)
                resp.append(str(curr.left.val))
            if curr.right is None:
                resp.append("X")
            else:
                bfsQueue.put(curr.right)
                resp.append(str(curr.right.val))
        return ','.join(resp)

    def deserialize(self, data):
        if not data or data =="":
            return None
        nodes = data.split(",")
        bfsQueue = queue.Queue()
        root = TreeNode(int(nodes[0]))
        bfsQueue.put(root)
        i = 1

        while i < len(nodes) and bfsQueue.qsize() > 0:
            curr = bfsQueue.get()
            if nodes[i] == "X":
                curr.left = None
            else:
                curr.left = TreeNode(int(nodes[i]))
                bfsQueue.put(curr.left)
            i += 1
            if i < len(nodes) and nodes[i] == "X":
                curr.right = None
            else:
                curr.right = TreeNode(int(nodes[i]))
                bfsQueue.put(curr.right)
            i += 1
        return root

if __name__ == '__main__':
    root = TreeNode(11, TreeNode(12, TreeNode(1), TreeNode(4)), TreeNode(7, None, TreeNode(9)))
    root2 = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))

    codecBFS = CodecBFS()
    serialized = codecBFS.serialize(root2)
    print(serialized)
    deserialized = codecBFS.deserialize(serialized)
    serialized = codecBFS.serialize(deserialized)
    print(serialized)

    codecDFS = CodecDFS()
    serialized = codecDFS.serialize(root2)
    print(serialized)
    deserialized = codecDFS.deserialize(serialized)
    serialized = codecDFS.serialize(deserialized)
    print(serialized)