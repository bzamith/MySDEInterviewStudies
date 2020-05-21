import queue

class GraphNode():
	def __init__(self, value):
		self.value = value
		self.neighbors = list()

	def addNeighbor(self, graphNode):
		self.neighbors.append(graphNode)
		graphNode.neighbors.append(self)

	def searchBFS(self, value):
		bfSearch = BreadthFirstSearch()
		return bfSearch.searchValue(self, value)

	def searchDFS(self, value):
		dfSearch = DepthFirstSearch()
		return dfSearch.searchValue(self, value)

	def getPathBFS(self, value):
		bfSearch = BreadthFirstSearch()
		return bfSearch.searchValuePath(self, value)

	def getPathDFS(self, value):
		dfSearch = DepthFirstSearch()
		return dfSearch.searchValuePath(self, value)

class BreadthFirstSearch():
	def __init__(self):
		self.queue = queue.Queue()
		self.pathQueue = queue.Queue()
		self.visited = {}

	def searchValue(self, root, value):
		self.queue.put(root)
		while not self.queue.empty():
			curr = self.queue.get()
			self.visited[curr] = True
			if curr.value == value:
				return curr
			for neighbor in curr.neighbors:
				if not neighbor in self.visited:
					self.queue.put(neighbor)
		return None

	def searchValuePath(self, root, value):
		self.queue.put(root)
		self.pathQueue.put([root.value])
		self.visited[root] = True
		while not self.queue.empty():
			curr = self.queue.get()
			currPath = self.pathQueue.get()
			self.visited[curr] = True
			if curr.value == value:
				return currPath
			for neighbor in curr.neighbors:
				if neighbor not in self.visited:
					self.queue.put(neighbor)
					self.pathQueue.put([neighbor.value] + currPath)
		return None

class DepthFirstSearch():
	def __init__(self):	
		self.visited = {}

	def searchValue(self, root, value):
		if root is None:
			return None
		if root.value == value:
			return root
		self.visited[root] = True
		for neighbor in root.neighbors:
			if not neighbor in self.visited:
				returnValue = self.searchValue(neighbor, value)
				if returnValue is not None:
					return returnValue
		return None

	def searchValuePath(self, root, value, currPath = list()):
		if root is None:
			return None
		currPath = [root.value] + currPath
		if root.value == value:
			return currPath
		self.visited[root] = True
		for neighbor in root.neighbors:
			if not neighbor in self.visited:
				returnValue = self.searchValuePath(neighbor, value, currPath)
				if returnValue is not None:
					return returnValue
		return None

if __name__ == "__main__":
	nodeA = GraphNode('a')
	nodeB = GraphNode('b')
	nodeC = GraphNode('c')
	nodeD = GraphNode('d')
	nodeE = GraphNode('e')
	nodeF = GraphNode('f')
	nodeG = GraphNode('g')
	nodeH = GraphNode('h')
	nodeI = GraphNode('i')
	nodeJ = GraphNode('j')
	nodeK = GraphNode('k')
	nodeA.addNeighbor(nodeB)
	nodeA.addNeighbor(nodeC)
	nodeA.addNeighbor(nodeD)
	nodeB.addNeighbor(nodeE)
	nodeC.addNeighbor(nodeF)
	nodeD.addNeighbor(nodeG)
	nodeE.addNeighbor(nodeH)
	nodeE.addNeighbor(nodeI)
	nodeG.addNeighbor(nodeI)
	nodeG.addNeighbor(nodeJ)
	nodeH.addNeighbor(nodeK)
	nodeI.addNeighbor(nodeK)
	print(nodeA.getPathBFS('g'))
	print(nodeA.getPathDFS('g'))
