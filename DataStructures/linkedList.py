import queue

def intersectionOfTwoLinkedLists(linkedList1, linkedList2):
	linkedList1.reverse()
	linkedList2.reverse()

	pointer1 = linkedList1.head
	pointer2 = linkedList2.head

	if pointer1.value != pointer2.value:
		return None

	while pointer1.value == pointer2.value and pointer1.next is not None and pointer2.next is not None:
		pointer1 = pointer1.next
		pointer2 = pointer2.next
	
	return pointer1.value

def intersectionOfTwoLinkedListsMethod2(linkedList1, linkedList2):
	linkedList1.reverse()
	linkedList2.reverse()

	pointer1 = linkedList1.head
	pointer2 = linkedList2.head

	if pointer1.value != pointer2.value:
		return None

	while pointer1.value == pointer2.value and pointer1.next is not None and pointer2.next is not None:
		pointer1 = pointer1.next
		pointer2 = pointer2.next
	
	return pointer1.value

class LinkedList():
	def __init__(self, value):
		self.head = LinkedListNode(value)

	def append(self, value):
		curr = self.head
		while curr.next is not None:
			curr = curr.next
		curr.next = LinkedListNode(value)

	def remove(self, value):
		if self.head.value == value:
			self.head = self.head.next
			self.head.prev = None
			return
		curr = self.head
		while curr.next is not None:
			if curr.next.value == value:
				curr.next = curr.next.next
				return
			curr = curr.next

	def removeFirst(self):
		self.head = self.head.next
		self.head.prev = None

	def reverse(self):
		prev = None
		curr = self.head 
		while(curr is not None): 
			nextOne = curr.next
			curr.next = prev 
			prev = curr 
			curr = nextOne
		self.head = prev 

	def isPalindrome(self):
		lazy = self.head
		runner = self.head
		while runner.next is not None and runner.next.next is not None:
			lazy = lazy.next
			runner = runner.next.next
		lazy = lazy.next
		stack = queue.LifoQueue()
		while lazy is not None:
			stack.put(lazy)
			lazy = lazy.next
		curr = stack.get()
		lazy = self.head
		while curr.value == lazy.value and not stack.empty():
			curr = stack.get()
			lazy = lazy.next
		if stack.empty():
			return True
		return False

	def print(self):
		curr = self.head
		while curr is not None:
			print(curr.value, end = ' -> ')
			curr = curr.next
		print('.')

class DoubleLinkedList():
	def __init__(self, value):
		self.head = LinkedListNode(value)

	def append(self, value):
		curr = self.head
		while curr.next is not None:
			curr = curr.next
		curr.next = LinkedListNode(value)
		curr.next.prev = curr

	def remove(self, value):
		if self.head.value == value:
			self.head = self.head.next
			return
		curr = self.head
		while curr.next is not None:
			if curr.next.value == value:
				curr.next = curr.next.next
				if curr.next is not None:
					curr.next.prev = curr
				return
			curr = curr.next

	def removeFirst(self):
		self.head = self.head.next

	def print(self):
		curr = self.head
		while curr is not None:
			print(curr.value, end = ' <-> ')
			curr = curr.next
		print('.')

class LinkedListNode():
	def __init__(self, value):
		self.value = value
		self.next = None
		self.prev = None

if __name__ == "__main__":
	linkedList = LinkedList(9)
	linkedList.append(7)
	linkedList.append(6)
	linkedList.append(1)
	linkedList.append(3)
	linkedList.append(5)
	linkedList.append(12)
	linkedList.append(29)
	linkedList.append(2)
	linkedList.append(36)
	linkedList.append(9)
	linkedList.print()
	linkedList.removeFirst()
	linkedList.removeFirst()
	linkedList.print()
	linkedList.remove(12)
	linkedList.remove(9)
	linkedList.print()
	linkedList.reverse()
	linkedList.print()
	print(linkedList.isPalindrome())

	doubleLinkedList = DoubleLinkedList(9)
	doubleLinkedList.append(7)
	doubleLinkedList.append(6)
	doubleLinkedList.append(1)
	doubleLinkedList.append(3)
	doubleLinkedList.append(5)
	doubleLinkedList.append(12)
	doubleLinkedList.print()
	doubleLinkedList.removeFirst()
	doubleLinkedList.removeFirst()
	doubleLinkedList.print()
	doubleLinkedList.remove(12)
	doubleLinkedList.print()

	evenPalindromeLinkedList = LinkedList(1)
	evenPalindromeLinkedList.append(2)
	evenPalindromeLinkedList.append(3)
	evenPalindromeLinkedList.append(3)
	evenPalindromeLinkedList.append(2)
	evenPalindromeLinkedList.append(1)
	evenPalindromeLinkedList.print()
	print(evenPalindromeLinkedList.isPalindrome())

	oddPalindromeLinkedList = LinkedList(1)
	oddPalindromeLinkedList.append(2)
	oddPalindromeLinkedList.append(3)
	oddPalindromeLinkedList.append(4)
	oddPalindromeLinkedList.append(3)
	oddPalindromeLinkedList.append(2)
	oddPalindromeLinkedList.append(1)
	oddPalindromeLinkedList.print()
	print(oddPalindromeLinkedList.isPalindrome())

	linkedList1 = LinkedList('a')
	linkedList1.append('b')
	linkedList1.append('c')
	linkedList1.append('d')
	linkedList1.append('n')
	linkedList1.append('o')
	linkedList1.append('p')

	linkedList2 = LinkedList('g')
	linkedList2.append('t')
	linkedList2.append('n')
	linkedList2.append('o')
	linkedList2.append('p')

	linkedList3 = LinkedList('g')
	linkedList3.append('t')
	linkedList3.append('s')
	linkedList3.append('a')
	linkedList3.append('t')

	print(intersectionOfTwoLinkedLists(linkedList1, linkedList2))
	print(intersectionOfTwoLinkedLists(linkedList1, linkedList3))
	print(intersectionOfTwoLinkedLists(linkedList1, linkedList1))




