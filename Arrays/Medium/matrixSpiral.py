"""
Problem Statement: Print the matrix in spiral manner

Given an M * N matrix, print the elements in a clockwise spiral 
manner. Return an array with the elements in the order of their 
appearance when printed in a spiral manner.


Examples:

1.  Input: matrix = [[1, 2, 3], [4 ,5 ,6], [7, 8, 9]]
    Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
    Explanation: The elements in the spiral order are 1, 2, 3 -> 6, 9 -> 8, 7 -> 4, 5

2.  Input: matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
    Output: [1, 2, 3, 4, 8, 7, 6, 5]
    Explanation: The elements in the spiral order are 1, 2, 3, 4 -> 8, 7, 6, 5

3.  Input: matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
    Output:[1, 2, 4, 6, 8, 7, 5, 3]
"""

def spiralMatrixOptimal(matrix):
    n = len(matrix)
    m = len(matrix[0])

    res = []

    top, left = 0, 0
    bottom, right = n - 1, m - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            res.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
    
    return res


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

res = spiralMatrixOptimal(matrix=matrix)
print(res)

"""
Approach:
    Theres is no multiple approaches to this problem, there exists only one solution to this
    problem, that is using the method that we used in this solution, this problem doesn't contain
    much of a logic, we can easily figure out the logic, but this problem is more concentrated to
    test out our implementation skills, so we just have to traverse from left -> right, top -> bottom,
    right -> left and finally we traverse from bottom -> top and we repeat this till bottom exceeds 
    the top or the right exceeds the left.

    Time -> O(MxN) => Since we are just going through each element once, we are visiting mxn elements
    and we are not using extra space, since the output requires the output array we cannot count that as
    extra space, so we can conclude this problem with the space complexity of
    
    Space -> O(1)
"""