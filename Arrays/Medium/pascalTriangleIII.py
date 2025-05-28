"""
Problem Statement:
    Given an integer n, return the first n (1-Indexed) rows of Pascal's triangle.

1.  Input: n = 4
    Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    Explanation: The Pascal's Triangle is as follows:

    1

    1 1

    1 2 1

    1 3 3 1

    1st Row has its value set to 1.
    All other cells take their value as the sum of the values directly above them

2.  Input: n = 5
    Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    Explanation: The Pascal's Triangle is as follows:

    1

    1 1

    1 2 1

    1 3 3 1

    1 4 6 4 1
    1st Row has its value set to 1.
    All other cells take their value as the sum of the values directly above them

3.  Input: n = 3
    Output:[[1], [1, 1], [1, 2, 1]]
"""

def generateRow(r):
    res = [1] * r

    for i in range(1, r - 1):
        res[i] = (res[i - 1] * (r - i)) // i
    
    return res

def pascalTriangleIII(r):
    res = []

    for i in range(1, r + 1):
        row = generateRow(i)
        res.append(row)
    
    return res

n = 4

res = pascalTriangleIII(n)
print(res)

"""
Approach:
    The solution to this problem is quite obvious, doesnt need much of an explanation,
    we just combine the II problem with this, generate row as we did for the pascal's
    traingle II, and we combine all rows from 1 to n and put that in another array
    and we just return that 2d array as the output

    Time -> O(n ** 2) (since we are genearate n rows of n elements)
    Space -> O(n ** 2 ) ( I think i need better clarity understanding this (Will update after some research))
"""