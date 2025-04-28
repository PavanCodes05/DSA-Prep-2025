"""
Problem Statement: Given an integer array nums and a non-negative integer k, rotate the array to the left by k steps.

TC:
1.  Input: nums = [1, 2, 3, 4, 5, 6], k = 2
    Output: nums = [3, 4, 5, 6, 1, 2]
    Explanation: rotate 1 step to the left: [2, 3, 4, 5, 6, 1]
    rotate 2 steps to the left: [3, 4, 5, 6, 1, 2]

2.  Input: nums = [3, 4, 1, 5, 3, -5], k = 8
    Output: nums = [1, 5, 3, -5, 3, 4]
    Explanation: rotate 1 step to the left: [4, 1, 5, 3, -5, 3]
    rotate 2 steps to the left: [1, 5, 3, -5, 3, 4]
    rotate 3 steps to the left: [5, 3, -5, 3, 4, 1]
    rotate 4 steps to the left: [3, -5, 3, 4, 1, 5]
    rotate 5 steps to the left: [-5, 3, 4, 1, 5, 3]
    rotate 6 steps to the left: [3, 4, 1, 5, 3, -5]
    rotate 7 steps to the left: [4, 1, 5, 3, -5, 3]
    rotate 8 steps to the left: [1, 5, 3, -5, 3, 4]
"""

nums = [3, 4, 1, 5, 3, -5]
k = 8

# Approach 1 (Brute Force)

def leftRotateArrayByKPlaces1(nums, k):
    n = len(nums)
    # Helps reducing the number of cycles by remove repetetion
    k = k % n

    while k > 0:
        tmp = nums[0]

        for i in range(1, n):
            nums[i - 1] = nums[i]
        
        nums[-1] = tmp
        
        k -= 1


# Approach 2 (Optimal)
def reverseArray(nums, start, end):
    while start < end:
        tmp = nums[start]

        nums[start] = nums[end]
        nums[end] = tmp

        start += 1
        end -= 1

def leftRotateByKPlaces(nums, k):
    n = len(nums)

    # Helps reducing the number of cycles by remove repetetion
    k = k % n

    # Reverse the first 'k' elements 
    reverseArray(nums, 0, k - 1)
    # Reverse the last k - n elements
    reverseArray(nums, k, n - 1)

    # Reverse the entire array
    reverseArray(nums, 0, n - 1)

leftRotateByKPlaces(nums, k) # Approach 2 (Optimal)
print(nums)

"""
Approach 1: This is the very first brute force approach that 
came to my mind, this approach is the same approach we used
in the previous problem `leftRotateArrayByOne`, this approach
is basically shifting elements and pushing the first ele to the 
last till k exists.

Approach 2: This is the optimal solution that I found online, 
being honest if I haven't looked for this online, I would have never
came up with this approach, it is about reversing, I have to read the
thinking behind it much further, but this solves the problem in a much 
efficient way.

Time: O(n ** 2) for approach 1, O(n) for approach 2
Space: O(1) for both approaches
"""