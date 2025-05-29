"""
Problem Statement:
    Given an N * N 2D integer matrix, rotate the matrix by 90 degrees clockwise.
    The rotation must be done in place, meaning the input 2D matrix must be 
    modified directly.

1.  Input: matrix = [[1, 1, 2], [5, 3, 1], [5, 3, 5]]
    Output:[[5, 5, 1], [3, 3, 1], [5, 1, 2]]

    (Other TC's are given as pictures, refer: https://takeuforward.org/plus/dsa/arrays/faqs-medium/rotate-matrix-by-90-degrees)
    
"""

def rotateMatrix90Brute(matrix):
    n = len(matrix)

    rotated = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated[j][n - i - 1] = matrix[i][j]
    
    for i in range(n):
        matrix[i] = rotated[i]
    
    return matrix
 

def rotateMatrix90Optimal(matrix):
    n = len(matrix)
    
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] =  matrix[j][i], matrix[i][j]
        
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j] 

    return matrix

matrix = [[1, 1, 2], [5, 3, 1], [5, 3, 5]]

# resBrute = rotateMatrix90Brute(matrix)
# print(resBrute)

resOptimal = rotateMatrix90Optimal(matrix)
print(resOptimal)

"""
Approach: I need a bit of time with pen and paper for a better understanding,
I can understand it now but I think it would be better if I can have a dry run
when i have access to pen and paper, so im leaving this incomplete for now.
"""