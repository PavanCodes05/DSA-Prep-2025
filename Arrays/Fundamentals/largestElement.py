""""
Problem Statement: Given an array of integers nums, return the value of the 
largest element in the array.

TC:
1.  Input: nums = [3, 3, 6, 1]
    Output: 6
    Explanation: The largest element in array is 6

2.  Input: nums = [3, 3, 0, 99, -40]
    Output: 99
    Explanation: The largest element in array is 99
"""

nums = [3, 3, 6, 1]

# Type 1
def largestElement1(nums):
    return max(nums)

# Type 2
def largestElement2(nums):
    # Consider the first value to be the largest
    maxVal = nums[0]
    # loop through and update the maxVal 
    for num in nums:
        # Compare the current val with the maxVal and update with larger one
        maxVal = max(num, maxVal)
    
    return maxVal

res1 = largestElement1(nums)
res2 = largestElement2(nums)

print(res1)
print(res2)


"""
Approach: These problems are just for getting us into DSA, I know these problems
are just there to keep us feeling good for a while, can't wait to experience the
actual DSA problems, but approach to this was pretty simple, I came up with two
different solutions but the changes are only with the lines of code but gives the 
same time and space complexity

1: We just find the maximum value in the array using the built-in function max()
2: It is the same as the first one, but here we do it manually, that is the 
   only difference

Time: O(n) -> We traverse and compare each element in the array to find maxVal.
Space: O(1) -> We are not using any extra space in these solutions.
"""