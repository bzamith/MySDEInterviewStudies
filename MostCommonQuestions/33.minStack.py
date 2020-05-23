# Source: https://leetcode.com/problems/min-stack/submissions/

# Problem: "Min Stack"

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#    push(x) -- Push element x onto stack.
#    pop() -- Removes the element on top of the stack.
#    top() -- Get the top element.
#    getMin() -- Retrieve the minimum element in the stack.

# Approach:
# For each state in the stack, store the current min value

class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((x,x))
        else:
            currMin = min(x,self.getMin())
            self.stack.append((x,currMin))

    def pop(self) -> None:
        resp = self.stack.pop()
        return resp[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

if __name__ == "__main__":
    obj = MinStack()
    obj.push(x)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()