# Source: https://www.youtube.com/watch?v=Wg8IiY1LbII

# Problem: "Implement a queue with stack(s)"

class Queue:  
    def __init__(self): 
        self.stack1 = [] 
        self.stack2 = [] 
  
    def enQueue(self, x): 
        # Move all elements from stack1 to stack2  
        while len(self.stack1) != 0:  
            self.stack2.append(self.stack1[-1])  
            self.stack1.pop() 
  
        # Push item into self.stack1  
        self.stack1.append(x)  
  
        # Push everything back to stack1  
        while len(self.stack2) != 0:  
            self.stack1.append(self.stack2[-1])  
            self.stack2.pop() 
  
    # Dequeue an item from the queue  
    def deQueue(self): 
        # if first stack is empty  
        if len(self.stack1) == 0:  
            print("Q is Empty") 
      
        # Return top of self.stack1  
        x = self.stack1[-1]  
        self.stack1.pop()  
        return x 
  
if __name__ == '__main__': 
    q = Queue() 
    q.enQueue(1)  
    q.enQueue(2)  
    q.enQueue(3)  
  
    print(q.deQueue()) 
    print(q.deQueue()) 
    print(q.deQueue()) 