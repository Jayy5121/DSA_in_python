def rotateImage(matrix):
    n=len(matrix)
    for i in range(n-1):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for num in matrix:
        num.reverse()
    return matrix
print(rotateImage([[1,2,3],[4,5,6],[7,8,9]]))