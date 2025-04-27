"""
Problem Statement: Given an array of integers nums and an integer target, 
find the smallest index (0 based indexing) where the target appears in the array. 
If the target is not found in the array, return -1

TC:
1.  Input: nums = [2, 3, 4, 5, 3], target = 3
    Output: 1
    Explanation: The first occurence of 3 in nums is at index 1

2.  Input: nums = [2, -4, 4, 0, 10], target = 6
    Output: -1
    Explanation: The value 6 does not occur in the array, hence output is -1
"""

nums = [2, 3, 4, 5, 3]
target = 3

def linearSearch(nums, target):
    # Traverse through the array
    for idx, num in enumerate(nums):
        # Check if the current value of the loop matches the target
        if num == target:
            # Return the index of the matching element
            return idx
    # Even after the loop through entire array if the value isn't returned, we return -1 as required in the PS
    return -1

res_idx = linearSearch(nums, target)
print(res_idx)

"""
Approach: The approach to solve this problem is pretty straightforward, 
because as the category says, it is a fundamental array problem, 
which can be solved pretty simply, just be traversing through the array 
and just checking each number with the target and returning the found idx (or) -1 if not found

Time: O(n) -> As we traverse through the entire array (In the worst case the element 
might be found in the last index)
Space: O(1) -> We are not using any extra space, just some constant space operations
"""