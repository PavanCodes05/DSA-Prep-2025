"""
Problem Statement:
    Given an integer r, return all the values in the rth row (1-indexed) 
    in Pascal's Triangle in correct order.

1.  Input: r = 4
    Output: [1, 3, 3, 1]
    Explanation: The Pascal's Triangle is as follows:

    1

    1 1

    1 2 1

    1 3 3 1
    ....
    Thus the 4th row is [1, 3, 3, 1]

2.  Input: r = 5
    Output: [1, 4, 6, 4, 1]
    Explanation: The Pascal's Triangle is as follows:

    1

    1 1

    1 2 1

    1 3 3 1

    1 4 6 4 1
    ....
    Thus the 5th row is [1, 4, 6, 4, 1]

3.  Input: r = 6
    Output: [1, 5, 10, 10, 5, 1]
"""

def pascalTriangleIIOptimal(r):
    res = [1] * r

    for i in range(1, r - 1):
        res[i] = (res[i - 1] * (r - i)) // i
    
    return res

n = 6

res = pascalTriangleIIOptimal(n)
print(res)


"""
Approach:
    This is the continuation of the previous problem that we have solved,
    we have to print the row of then given `n` from the pascal's triangle

    There are many ways to do this, but we just chose to go with the optimal one
    because the brute force lies in the previous and next problem, so we do not
    need to use it over and over again.

    The logic behind this is, understanding the pattern behind it, we can clearly see some
    pattern in the row, take a piece of paper and pen to draw out the pascal triangle, and pick the
    row and find the pattern

    We know it for sure that the first and last element is going to be 1, so we create a array of
    size 'n' full of ones(1's), we just loop through the remaining elements to update the new values

    The underlying pattern is, (prev * (row - column)) // column

    Using this formula we can arrive at the solution.

    Time => O(R)
    Space => O(1)
"""