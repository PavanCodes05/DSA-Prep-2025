"""
Problem Statement: Given an integer array nums, rotate the 
array to the left by one.

Note: There is no need to return anything, just modify the given array.

Tc:
1.  Input: nums = [1, 2, 3, 4, 5]
    Output: [2, 3, 4, 5, 1]
    Explanation: Initially, nums = [1, 2, 3, 4, 5]
    Rotating once to left -> nums = [2, 3, 4, 5, 1]

2.  Input: nums = [-1, 0, 3, 6]
    Output: [0, 3, 6, -1]
    Explanation: Initially, nums = [-1, 0, 3, 6] 
    Rotating once to left -> nums = [0, 3, 6, -1]
"""

nums = [1, 2, 3, 4, 5]

def leftRotateByOne(nums):
    # Storing the left most element on a temp var
    tmp = nums[0]

    # Traverse through the array and shift elem to the left by one place
    for i in range(1, len(nums)):
        nums[i - 1] = nums[i]
    # Assign the tmp value to the last element of the array.
    nums[-1] = tmp

"""
Approach: The fundamental problems are pretty basic and very 
easy to do and doesn't need much of an explantion. it is just
shifting elements to the left and replacing the last value

Time: O(n)
Space = O(1)
"""