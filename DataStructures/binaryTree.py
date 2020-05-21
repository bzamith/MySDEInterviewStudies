import queue

class BinarySearch():
	def __init__(self, binaryTree):
		self.binaryTree = binaryTree

	def searchValueEquaTo(self, value):
		return self.recursiveSearchValueEqualTo(self.binaryTree.root, value)

	def recursiveSearchValueEqualTo(self, root, value):
		if root == None:
			return None
		if root.value == value:
			return root
		if root.value > value:
			return self.recursiveSearchValueEqualTo(root.left, value)
		return self.recursiveSearchValueEqualTo(root.right, value)

class DepthFirstSearch():
	def __init__(self, binaryTree):
		self.stack = queue.LifoQueue() #stack
		self.binaryTree = binaryTree

	def searchValueEquaTo(self, value):
		self.stack.put(self.binaryTree.root)
		while not self.stack.empty():
			curr = self.stack.get()
			if curr.value == value:
				return curr
			if curr.left is not None:
				self.stack.put(curr.left)
			if curr.right is not None:
				self.stack.put(curr.right)
		return None

class BreadthFirstSearch():
	def __init__(self, binaryTree):
		self.queue = queue.Queue()
		self.binaryTree = binaryTree

	def searchNbChildrenLessThan(self, value):
		self.queue.put(self.binaryTree.root)
		while not self.queue.empty():
			curr = self.queue.get()
			if curr.nbChildren < value:
				return curr
			if curr.left is not None:
				self.queue.put(curr.left)
			if curr.right is not None:
				self.queue.put(curr.right)
		return None

	def searchValueEquaTo(self, value):
		self.queue.put(self.binaryTree.root)
		while not self.queue.empty():
			curr = self.queue.get()
			if curr.value == value:
				return curr
			if curr.left is not None:
				self.queue.put(curr.left)
			if curr.right is not None:
				self.queue.put(curr.right)
		return None

class BinaryTree():
	def __init__(self, value):
		self.root = BinaryNode(value)

	def printTree(self):
		self.recursivePrintTree(self.root)

	def recursivePrintTree(self, root):
		if root is None:
			return
		self.recursivePrintTree(root.left)
		print(root.value)
		self.recursivePrintTree(root.right)

	def insertNode(self, node):
		bfSearch = BreadthFirstSearch(self)
		parentNode = bfSearch.searchNbChildrenLessThan(2)
		if parentNode.nbChildren == 0:
			parentNode.left = node
		else:
			parentNode.right = node
		parentNode.nbChildren += 1

	def findValue(self, value):
		dfSearch = DepthFirstSearch(self)
		return dfSearch.searchValueEquaTo(value)

	def getHeights(self, node):
		self.recursiveGetHeights(self.root)
		return node.height

	def recursiveGetHeights(self, root):  
		if root is None:
			return 0
		else:
			hLeft = self.recursiveGetHeights(root.left)
			hRight = self.recursiveGetHeights(root.right)
			if (hLeft > hRight):  
				root.height = (hLeft + 1)  
			else: 
				root.height = (hRight + 1)
			return root.height

class BinarySearchTree(BinaryTree):
	def __init__(self, value):
		self.root = BinaryNode(value)

	def insertNode(self, node):
		self.recursiveInsertNode(self.root, node)

	def recursiveInsertNode(self, root, node):
		if node.value == root.value:
			return
		if root.value > node.value:
			if root.left is None:
				root.left = node
			else:
			 	self.recursiveInsertNode(root.left, node)
		else:
			if root.right is None:
				root.right = node
			else:
				self.recursiveInsertNode(root.right, node)

	def findValue(self, value):
		bSearch = BinarySearch(self)
		return bSearch.searchValueEquaTo(value)

class BinaryNode():
	def __init__(self, value, left = None, right = None):
		self.value = value
		self.left = left
		self.right = right
		self.nbChildren = 0
		self.height = 0
		if left is not None:
			self.nbChildren += 1
			self.height = self.left.height + 1
		if right is not None:
			self.nbChildren += 1
			self.height = self.right.height + 1

if __name__ == "__main__":
	tree = BinaryTree(100)
	tree.insertNode(BinaryNode(190))
	tree.insertNode(BinaryNode(75))
	tree.insertNode(BinaryNode(90))
	tree.insertNode(BinaryNode(140))
	tree.insertNode(BinaryNode(60))
	tree.insertNode(BinaryNode(30))
	tree.insertNode(BinaryNode(120))
	tree.insertNode(BinaryNode(160))
	tree.insertNode(BinaryNode(65))
	tree.printTree()
	print(tree.findValue(300) is None)
	print(tree.findValue(90) is None)
	print(tree.getHeights(BinaryNode(160)))

