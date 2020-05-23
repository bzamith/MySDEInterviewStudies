# Source: https://www.youtube.com/watch?v=S6IfqDXWa10

# Problem: "Implement a LRU Cache"

# Example: 
#  "LRU" = Last Resource Used

# Approach:
# We need fast lookup = HashTable
# We need fast insert in the end and removal = Doubly Linked List

class LinkedListNode():
	def __init__(self,value, prev=None, next=None):
		self.value = value
		self.prev = prev
		self.next = next

class CacheLRU():
	def __init__(self,size):
		self.size = size
		self.hash = {}
		self.listStart = None
		self.listEnd = None
	def add(self,value):
		# If hash is empty
		if len(self.hash.keys()) == 0:
			node = LinkedListNode(value)
			self.listStart = node
			self.listEnd = node
			self.hash[value] = node
		# If value is not in hash
		elif value not in self.hash:
			node = LinkedListNode(value)
			# If hash isn't full
			if len(self.hash.keys()) < self.size:
				self.insertInLinkedList(node)
				self.hash[value] = node
			# If hash is full
			else:
				self.removeFromLinkedListEnd()
				self.insertInLinkedList(node)
				self.hash[value] = node
		# If value is in hash
		else:
			node = self.hash[value]
			# If value isn't already the first one
			if self.listStart != node:
				self.removeFromLinkedList(node)
				self.insertInLinkedList(node)
	def insertInLinkedList(self,node):
		self.listStart.prev = node
		node.next = self.listStart
		self.listStart = node
	def removeFromLinkedListEnd(self):
		del self.hash[self.listEnd.value]
		self.listEnd.prev.next = None
		self.listEnd = self.listEnd.prev
	def removeFromLinkedList(self, node):
		node.prev.next = node.next
		if node.next == None:
			self.listEnd = node.prev
		else:
			node.next.prev = node.prev
	def print(self):
		node = self.listStart
		while node != None:
			print(node.value, end=" -> ")
			node = node.next
		print("null")
				
if __name__ == "__main__":
	myCacheLRU = CacheLRU(3)
	print("* Empty")
	myCacheLRU.print()
	print("* Add 2")
	myCacheLRU.add(2)
	myCacheLRU.print()
	print("* Add 2")
	myCacheLRU.add(2)
	myCacheLRU.print()
	print("* Add 3")
	myCacheLRU.add(3)
	myCacheLRU.print()
	print("* Add 4")
	myCacheLRU.add(4)
	myCacheLRU.print()
	print("* Add 5")
	myCacheLRU.add(5)
	myCacheLRU.print()
	print("* Add 2")
	myCacheLRU.add(2)
	myCacheLRU.print()
	print("* Add 5")
	myCacheLRU.add(5)
	myCacheLRU.print()
	print("* Add 5")
	myCacheLRU.add(5)
	myCacheLRU.print()
	print("* Add 4")
	myCacheLRU.add(4)
	myCacheLRU.print()

