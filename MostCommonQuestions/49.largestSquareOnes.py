def maximalSquare(self, matrix: List[List[str]]) -> int:
    maxSide=0
    if not matrix or len(matrix)==0:
        return 0
    nbRows = len(matrix)
    nbCols = len(matrix[0])
    
    dp=[[0 for i in range(nbCols)] for j in range(nbRows)]
    for row in range(nbRows):
        for col in range(nbCols):
            if (row==0 or col==0) and matrix[row][col]=="1":
                dp[row][col]=1
                if dp[row][col]>maxSide:
                    maxSide=dp[row][col]
            elif matrix[row][col]=="1":
                dp[row][col]=(1+min(dp[row-1][col-1],dp[row-1][col],dp[row][col-1]))
                if dp[row][col]>maxSide:
                    maxSide=dp[row][col]
    
    return maxSide*maxSide