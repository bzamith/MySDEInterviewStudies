class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, array):
        stack = []
        result = []
        for num in array:
            # see of there's integer smaller than num in the stack
            while stack and stack[-1] >= num:
                stack.pop()
            if stack:  # found the smaller integer
                result.append(stack[-1])
            else:  # stack is empty, smaller integer wasn't found
                result.append(-1)
            stack.append(num)  # push current num to the stack
        return result


class Solution2:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        lenA = len(A)
        if lenA == 1:
            return [-1]
        G = [-1 for i in range(lenA)]
        for i in range(lenA-1,0,-1):
            j = i - 1
            while j >= 0 and A[j] >= A[i]:
                j -= 1
            if j >= 0 and A[j] < A[i]:
                G[i] = A[j]
        return G