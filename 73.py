class Solution(object):
    def setZeroes(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        col0 = 1

        # First pass: mark rows and columns
        for i in range(n):
            if matrix[i][0] == 0:
                col0 = 0
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Second pass: apply zeroes using markers (skip first row and column)
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Handle first row
        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0

        # Handle first column
        if col0 == 0:
            for i in range(n):
                matrix[i][0] = 0

        return matrix