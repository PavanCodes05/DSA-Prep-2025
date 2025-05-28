"""
Problem Statement:
    Given two integers r and c, return the value at the rth row and 
    cth column (1-indexed) in a Pascal's Triangle.

    In Pascal's triangle:

    The first row has one element with a value of 1.
    Each row has one more element in it than its previous row.
    The value of each element is equal to the sum of the elements 
    directly above it when arranged in a triangle format.

1.  Input: r = 4, c = 2
    Output: 3
    Explanation: The Pascal's Triangle is as follows:
    1

    1 1

    1 2 1

    1 3 3 1
    ....
    Thus, value at row 4 and column 2 = 3

2.  Input: r = 5, c = 3
    Output: 6
    Explanation: The Pascal's Triangle is as follows:
    1

    1 1

    1 2 1

    1 3 3 1

    1 4 6 4 1
    ....
    Thus, value at row 5 and column 3 = 6

3.  Input: r = 6, c = 2
    Output: 5 
"""

def pascalTriangleIOptimal(r, c):
    return nCr(r - 1, c - 1)

def nCr(n, r):
    r = min(r, n - r)

    if r == 1:
        return n
    
    res = 1

    for i in range(r):
        res *= (n - i)
        res = res // (i + 1)
    
    return res

r = 6
c = 2

res = pascalTriangleIOptimal(r, c)
print(res)

"""
Approach:
    There are two different ways this can be solved but im just going to use the
    optimal one here because the brute solution of this problem is asked as a 
    question in another question (Pascal's Triangle III) so here we are only going
    to discuss about the optimal solution.

    The optimal solution depends on the formula of nCr, Combinatorics formula can help
    us solve the problem much in optimized way rather than the brute force

    `nCr = n! // r! * (n - r) !`

    The above formula should be used to arrive at the arrival of the optimized solution.
    
    But using the formula as it is going to give us O(2n + (n - r)) time complexity 
    which can be optimized much further.

    we know that the n - r always going to contain some part of n in it, so instead of 
    generating it and removing it later on we can just do not generate it, running the loop
    in only the size of r, ignoring the n in it, so we can now iterate only `r` times rather 
    than `n` times, this reduces the time further but we can further optimize it, but choosing the
    smallest value between `r` and `n-r` which can reduce the iterations further.

    IMPORTANT:
        We are supposed to divide each number on the numerator by 1,2,3 and so on in non-decreasing
        denominator, this step is more vital for us to arrive at the solution.

        eg: 10 // 1 * 9 // 2 * 8 // 3 ....
    
    Time -> O(min(r, n - r))
    Space -> O(1)
"""