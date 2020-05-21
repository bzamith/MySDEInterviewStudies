# Source: https://www.udemy.com/course/11-essential-coding-interview-questions/

# Problem: "Find the nth element from end in a linked list"

# Example: 
#  head = 5->4->3->2->1->0->null
#  nthFromEnd(head,4) = 3
#  nthFromEnd(head,7) = null
#  nthFromEnd(head,1) = null

# Brute-force solution:
# Traverse until the end, calculate length-n and traverse again

# Approach:
# Use a stack (Solution 2)
# Use 2 pointers (Solution 1), right and left. Move left n positions ahead 
# from right. Now move both until right reaches null. Return left.

# Complexity:
# O(N) time
# O(1) space

import queue

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next  = next 

def nthFromLastBestApproach(head, n):
    left = head
    right = head
    for i in range(n):
        if right == None:
            return None
        right = right.child
    while right:
        right = right.child
        left = left.child
    return left

def nthFromLast(head, n):
    if not head:
        return None
    stack = queue.LifoQueue()
    curr = head
    while curr:
        stack.put(curr.value)
        curr = curr.next 
    resp = 0
    if n > stack.qsize():
    	return None
    for i in range(n):
        resp = stack.get()
    return resp

if __name__ == "__main__":
    current = Node(1)
    for i in range(2, 8):
        current = Node(i, current)
    head = current
    # head = 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> (None)

    current2 = Node(4)
    for i in range(3, 0, -1):
        current2 = Node(i, current2)
    head2 = current2
    # head2 = 1 -> 2 -> 3 -> 4 -> (None)

    print(nthFromLast(head, 1)) #should return 1.
    print(nthFromLast(head, 5)) #should return 5.
    print(nthFromLast(head2, 2)) #should return 3.
    print(nthFromLast(head2, 4)) #should return 1.
    print(nthFromLast(head2, 5)) #should return None.
    print(nthFromLast(None, 1)) #should return None.