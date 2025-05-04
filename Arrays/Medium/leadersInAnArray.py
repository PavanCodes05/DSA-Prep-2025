"""
Problem Statement: Given an integer array nums, return a list of 
all the leaders in the array.

A leader in an array is an element whose value is strictly greater than
all elements to its right in the given array. The rightmost element is 
always a leader. The elements in the leader array must appear in the order 
they appear in the nums array.

TC:

1.  Input: nums = [1, 2, 5, 3, 1, 2]
    Output: [5, 3, 2]
    Explanation: 2 is the rightmost element, 3 is the largest element in the 
    index range [3, 5], 5 is the largest element in the index range [2, 5]
2.  Input: nums = [-3, 4, 5, 1, -4, -5]
    Output: [5, 1, -4, -5]
    Explanation: -5 is the rightmost element, -4 is the largest element in the 
    index range [4, 5], 1 is the largest element in the index range [3, 5] and 
    5 is the largest element in the range [2, 5]
"""
nums = [1, 2, 5, 3, 1, 2]

def leadersBrute(nums):
    # Resulting vector to store the leaders
    res =  []

    # We use a nested loop
    # Outer loop goes from 0-n
    for i in range(len(nums)):
        # We set a flag initially to true, so that the last element is already considered as a leader
        flag = True
        # We loop from i + 1 - n
        for j in range(i + 1, len(nums)):
            # If we see a greater element than the i, we change flag as false, and stop the loop
            if nums[j] > nums[i]:
                flag = False
                break
        # Add elements to res if the flag still remains true
        if flag:
            res.append(nums[i])
    # Finally return the resulting array
    return res

def leadersOptimal(nums):
    res = []
    
    # Last element is the maximum we start with
    maxVal = nums[-1]
    # The last element is always going to be a leader
    # Since it doesn't have any numbers to its right, so it is always going to be greatests
    res.append(maxVal)
    
    # We run a loop from n - 0
    for i in range(len(nums) - 1, -1, -1): 
        # If i see a greater value than max
        if nums[i] > maxVal:
            # I add that value to the leaders array
            res.append(nums[i])
            # Update the maxVal with new max
            maxVal = nums[i]
    # Since the order of occurance should not change, we must reverse the array before returning 
    return res[::-1]


leaders = leadersOptimal(nums)
print(leaders)

"""
Approach:
    Brute: The brute force solution for this problem is very easy to come up with, the tweaks
    in setting the flag 'True' or 'False' is kinda hypothetical, setting the flag initially
    'True' is a smart move, we dont have to explicitly add the last element, the loop will take
    care of it since the flag is gonna remain same and the inner loop ain't gonna run for the
    last element.

    Time: O(n ** 2)
    Space: O(1)

    Brute to Optimal: We can definitely work on the time complexity, we should find a way 
    to do this in a single iteration.

    Optimal: This is quite unique yet efficient solution, we start looking for elements from right
    to left, we consider the last element to be the maximum inititally, while looping if i see a greater
    value than the current maximum, it probably means that it is the greater value than any value on its
    right, which means it is a leader, so we add it to the resulting array and also update the maxVal value 
    with the current value and continue the search

    Time: O(n)
    Space: O(1)
"""