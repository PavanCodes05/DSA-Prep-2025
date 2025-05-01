"""
Problem Statement: Given an integer array of size n containing distinct values 
in the range from 0 to n (inclusive), return the only number missing from the array 
within this range.

TC:
1.  Input: nums = [0, 2, 3, 1, 4]
    Output: 5
    Explanation: nums contains 0, 1, 2, 3, 4 thus leaving 5 as the only missing 
    number in the range [0, 5]

2.  Input: nums = [0, 1, 2, 4, 5, 6]
    Output: 3
    Explanation: nums contains 0, 1, 2, 4, 5, 6 thus leaving 3 as the only 
    missing number in the range [0, 6]
"""

# Brute

nums = [0, 2, 3, 1, 4]

def findMissingNumberBrute(nums):
    # Sort the array
    nums.sort()

    # The array should start with a '0'
    if nums[0] != 0:
        # If not '0' is missing, so we return 0
        return 0
    
    # Traverse from first to last before element
    for i in range(len(nums) - 1):
        # If diff between the next and current elemnt is greater than one, the next element is missing
        if nums[i + 1] - nums[i] > 1:
            # We return the expected number to be there
            return i + 1
    
    # If end of loop, nothing is returned, the missing number is the n-th number
    return len(nums)

def findMissingNumberOptimal(nums):
    # We create a array of size 'n'- including n and find sum of it
    expected = sum([num for num in range(len(nums) + 1)])
    # We add up the current sum of the given arr
    actual = sum(nums)

    # We find the difference between them, and return the difference as the missing number
    res = expected - actual

    return res

missingNumber = findMissingNumberOptimal(nums)
print(missingNumber)


"""
Approach: 
    Brute: The brute force approach for this problem is quite confusing and not 
    so good of modular code, it is kind of hard coded and Iam not a big fan of it
    Still the intuition behind this solution is, if we sorted the array, we would have
    the difference of '1' between the elements but we have to check if the missing number
    is a '0' or 'n' so we do the check before and after the loop, if the first number is not
    a zero, probably zero is the missing one, and if nothing has returned in zero check and 
    the loop check, probably the n-th element is the missing one, so we return that end of loop

    Time: O(n ** 2) or o(n log n) based on the sorting algo we use
    Space: O(1)

    Optimal: The optimal solution is quite smart approach, we can find the sum of expected
    values 0 to n and find the sum of the given array, When we find the difference between
    them, we can easily find the missing number, we do not have to have any conditions for
    the edge cases, since a number will be missing guaranteed.

    Time: O(n)
    Space: O(1)
""" 