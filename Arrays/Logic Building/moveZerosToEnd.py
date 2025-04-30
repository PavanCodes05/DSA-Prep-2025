"""
Problem Statement: Given an integer array nums, move all 
the 0's to the end of the array. The relative order of the 
other elements must remain the same. This must be done in place, 
without making a copy of the array.

Tc:
1.  Input: nums = [0, 1, 4, 0, 5, 2]
    Output: [1, 4, 5, 2, 0, 0]
    Explanation: Both the zeroes are moved to the end and the order of the other elements stay the same

2.  Input: nums = [0, 0, 0, 1, 3, -2]
    Output: [1, 3, -2, 0, 0, 0]
    Explanation: All 3 zeroes are moved to the end and the order of the other elements stay the same
"""

# Brute

nums = [0, 1, 4, 0, 5, 2]

def moveZerosToEndBrute(nums):
    n = len(nums)
    # Create a array of 0's of size 'n'
    temp = [0] * n

    # Keep track of position to insert next non-zero ele
    pos = 0
    
    # Traverse through the array, find non-zero and place in temp arr
    for num in nums:
        if num != 0:
            temp[pos] = num
            pos += 1
    
    # Replace actual arr with temp elements
    for i in range(len(temp)):
        nums[i] = temp[i]
    
    return nums

# bruteSol = moveZerosToEndBrute(nums)

def moveZerosToEndOptimal(nums):
    # Init j as -1 to find out the first pos of zero
    j = -1

    # Find first pos of zero 
    for i in range(len(nums)):
        if nums[i] == 0:
            j = i
            break

    # If no zero found, return (as array is already in desired manner)
    if j == -1:
        return
    
    # Find non-zeros and swap it with zeros
    for i in range(j + 1, len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            # Make sure to move the j with the zero
            j += 1


moveZerosToEndOptimal(nums)
print(nums)

"""
Approach:

    Brute Force: The brute force solution is a pretty straightforward one, we can
    simply create a temp arr of same number of zeros as the length of the array
    and we can just add replace zeros with the non-zero elements, and leave rest of 
    the elements as zero, which actually solves the problem but, as the question asks
    we have to do it in-place, which means we have to modify the given arr, we cannot
    return a new one, so we replace every element of actual array with the temp arr.

    Time: O(n)
    Space: O(n) -> Using a temp array of same length

    Optimal: The optimal solution is quite smart one to go with, A two pointer approach
    one to find the position to place the next non-zero element we see, one to traverse 
    through the array to find the non-zero elements, We keep the j as -1 first, to find 
    the first occurance of the zero, which could be the first place to place our non-zero 
    element, now we start iterate from the next element of the first zero till end, and we 
    swap elements with zero whenever we see a non-zero element. We do not have to return
    anything since we are modifying the exact array.

    Time: O(n)
    Space: O(1) 
"""