# Source: https://www.youtube.com/watch?v=RVIh0snn4Qc

# Problem: "Largest Area in Histogram"

# Brute-force solution: Check every at left and every at right until smaller

# Approach: 
# 1) Create an empty stack.
# 2) Start from first bar, and do following for every bar ‘hist[i]’ where ‘i’ varies from 0 to n-1.
#    a) If stack is empty or hist[i] is higher than the bar at top of stack, then push ‘i’ to stack.
#    b) If this bar is smaller than the top of stack, then keep removing the top of stack while top of the stack is greater. 
#       Let the removed bar be hist[tp]. Calculate area of rectangle with hist[tp] as smallest bar. For hist[tp], the ‘left 
#       index’ is previous (previous to tp) item in stack and ‘right index’ is ‘i’ (current index).
# 3) If the stack is not empty, then one by one remove all bars from stack and do step 2.b for every removed bar.

def largestRectangleAreaBestApproach(heights):
    stack = list() 
    max_area = 0 
    index = 0
    while index < len(heights):       
        # If this bar is higher  
        # than the bar on top 
        # stack, push it to stack ]
        if (not stack) or (heights[stack[-1]] <= heights[index]): 
            stack.append(index) 
            index += 1
        # If this bar is lower than top of stack, 
        # then calculate area of rectangle with  
        # stack top as the smallest (or minimum 
        # height) bar.'i' is 'right index' for  
        # the top and element before top in stack 
        # is 'left index' 
        else: 
            # pop the top 
            top_of_stack = stack.pop() 
            # Calculate the area with  
            # heights[top_of_stack] stack 
            # as smallest bar 
            area = (heights[top_of_stack] * 
                   ((index - stack[-1] - 1)  
                   if stack else index)) 
            # update max area, if needed 
            max_area = max(max_area, area) 
    # Now pop the remaining bars from  
    # stack and calculate area with  
    # every popped bar as the smallest bar 
    while stack: 
        # pop the top 
        top_of_stack = stack.pop() 
        # Calculate the area with  
        # heights[top_of_stack]  
        # stack as smallest bar 
        area = (heights[top_of_stack] * 
              ((index - stack[-1] - 1)  
                if stack else index)) 
        # update max area, if needed 
        max_area = max(max_area, area) 
    # Return maximum area under  
    # the given histogram 
    return max_area 

def largestRectangleArea(heights):
    if not heights:
        return 0
    if len(heights) == 1:
        return heights[0]
    globalMax = 0
    for i in range(0,len(heights)):
        currCount = 1
        for j in range(i-1, -1, -1):
            if heights[j] < heights[i]:
                break
            else:
                currCount += 1 
        for j in range(i+1, len(heights)):
            if heights[j] < heights[i]:
                break
            else:
                currCount += 1
        currArea = currCount * heights[i]
        if currArea > globalMax:
            globalMax = currArea
    return globalMax
            
        