# Source: https://www.youtube.com/watch?v=zGv3hOORxh0

# Problem: "Find the area of overlapping triangles"

# Example: 
#  [x1,y1,x2,y2] and [k1,l1,k2,l2]
#  x1,y1 is the bottom-left and x2,y2 is the upper-right

# Approach:
# Check if width and height overlaps. Return the size of the
# overlap

# Complexity:
# O(1) time
# O(1) space

def sizeRectangleOverlap(rec1, rec2):
    if not rec1 or not rec2:
        return False
    if len(rec1) != 4 or len(rec2) != 4:
        return False
    width1 = (rec1[0],rec1[2])
    width2 = (rec2[0],rec2[2])
    height1 = (rec1[1],rec1[3])
    height2 = (rec2[1],rec2[3])
    overlapWidth = sizeOverlap(width1,width2)
    overlapHeight = sizeOverlap(height1,height2)
    if overlapWidth and overlapHeight:
    	return overlapWidth*overlapHeight
    return False

def isOverlap(side1,side2):
    # who starts first?
    if side1[0] <= side2[0]: 
    	first = side1
    	last = side2
    else:
    	first = side2
    	last = side1
    # first ends before last starts
    if first[1] <= last[0]:
    	return False
    return True

def sizeOverlap(side1,side2):
    # who starts first?
    if side1[0] <= side2[0]: 
    	first = side1
    	last = side2
    else:
    	first = side2
    	last = side1
    # first ends before last starts
    if first[1] <= last[0]:
    	return False
    else:
    	return first[1] - last[0]

if __name__ == "__main__":
    print(sizeRectangleOverlap([0,0,1,1],[1,0,2,1]))
    print(sizeRectangleOverlap([2,1,5,5],[3,2,5,7]))